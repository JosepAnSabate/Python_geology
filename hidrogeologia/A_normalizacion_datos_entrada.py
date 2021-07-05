#!/usr/bin/python 
# -*- coding: latin-1 -*-
import time
import pandas as pd 
from functools import reduce
import openpyxl
import os 

t1 = time.time()

os.chdir("C:/Users/34639/Desktop/curspython/hidro/Ejemplos_hidro/Ejemplos_hidro")

# Importacion de archivos
df_pou=pd.read_csv('data/Pou_pineda.csv', sep=';', skiprows=range(0, 11))#skiprows indica donde empiexa el csv. Comensa a la 12
df_pz1=pd.read_csv('data/PZ_Pineda.csv', sep=',', skiprows=range(0, 27))
df_pz2=pd.read_csv('data/PZ_Pineda_2.csv', sep=',', skiprows=range(0, 27))




print(df_pz1.columns) #imprimir columna

# Preprocesamos las tablas de entrada
# 1-POU
#pandas
##Eliminamos ms 
df_pou_norm = df_pou.drop(columns=['ms'])

df_pou_norm.columns=["Fecha","Hora","Presion_POU","Temperatura_POU"]
df_pou_norm["Fecha"]=pd.to_datetime(df_pou_norm["Fecha"],format="%d/%m/%Y").dt.date #canvia el format de la data
df_pou_norm["Hora"]=pd.to_datetime(df_pou_norm["Hora"]).dt.time #canvia format hora(no cal en aquest cas)
#separar les dades per punts en comptes de coma de les col Tpou o Ppou
#apply itera per cada un dels elements reemplasant , per .
#lambda https://www.w3schools.com/python/python_lambda.asp
df_pou_norm["Temperatura_POU"] = df_pou_norm["Temperatura_POU"].apply(lambda x: float(x.split()[0].replace(',', '.')))
df_pou_norm["Presion_POU"] = df_pou_norm["Presion_POU"].apply(lambda x: float(x.split()[0].replace(',', '.')))            
print(df_pou_norm.dtypes)

# PZ-1 drop col
df_pz1_norm = df_pz1.drop(columns=['Rec #'])
                                
df_pz1_norm["Fecha"] = pd.to_datetime(df_pz1_norm['Date / Time']).dt.date #crear col fecha a partir de Date /Time
df_pz1_norm["Hora"] = pd.to_datetime(df_pz1_norm['Date / Time']).dt.time

del df_pz1_norm['Date / Time'] #del delete col

df_pz1_norm.columns=["Temperatura_PZ1","Presion_PZ1","Fecha","Hora"]#renombrar els camps 0 i 1


# PZ-2 el mateix amb pz-2
df_pz2_norm = df_pz2.drop(columns=['Rec #'])
                                   
df_pz2_norm["Fecha"] = pd.to_datetime(df_pz2_norm['Date / Time']).dt.date
df_pz2_norm["Hora"] = pd.to_datetime(df_pz2_norm['Date / Time']).dt.time

del df_pz2_norm['Date / Time']

df_pz2_norm.columns=["Temperatura_PZ2","Presion_PZ2","Fecha","Hora"]

#imprimir el tipus de dades de totes les col normalitzades
print(df_pou_norm.dtypes)
print(df_pz1_norm.dtypes)
print(df_pz2_norm.dtypes)


#crear df
dfs = [df_pou_norm,df_pz1_norm,df_pz2_norm]
#unificar df
#reduce: ajunta taules de esq a dreta de esq a dreta
#camps d'unio fecha i hora , tenen que coincidir!
# lambda https://www.w3schools.com/python/python_lambda.asp
df_merged = reduce(lambda  left,right: pd.merge(left,right,on=["Fecha","Hora"],how='outer'), dfs)
#per cada fila afegir 60segons
df_merged["Segons"]= [*range(0,60*df_merged.shape[0],60)]
#ordenar els camps
df_merged = df_merged.reindex(['Fecha','Hora','Segons','Presion_POU','Temperatura_POU','Presion_PZ1','Temperatura_PZ1','Presion_PZ2','Temperatura_PZ2'], axis=1)


#fichero creado
df_merged.to_excel("data\df_sensores_unificado.xlsx",sheet_name='Sensores_Pineda',index=False)  


t2= time.time()

t_ejecucion= t2-t1

print ("Finalizado en %s"%(t_ejecucion))
