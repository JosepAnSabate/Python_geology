#!/usr/bin/python 
# -*- coding: latin-1 -*-
import time
import pandas as pd 
from functools import reduce
import numpy as np
import openpyxl
import os 
import warnings

os.chdir("C:/Users/34639/Desktop/curspython/hidro/Ejemplos_hidro/Ejemplos_hidro/")

t1 = time.time()

df = pd.read_excel("data\df_sensores_unificado.xlsx", sheet_name="Sensores_Pineda")

# Valor de correspondencia de H20 por 1PSI
v_psi_h20 = 0.70307

#Primeros valores de la columna descens
v_descenso_origen_pou= 4.38
v_descenso_origen_pz1= 4.435
v_descenso_origen_pz2= 4.462

cota_np_pou=4.96 
cota_np_pz1= 4.99
cota_np_pz2= 4.98




#                                                   H20
df["psi_POU"]=df["Presion_POU"]*v_psi_h20
df["psi_PZ1"]=df["Presion_PZ1"]*v_psi_h20
df["psi_PZ2"]=df["Presion_PZ2"]*v_psi_h20



#                                                Descensos
warnings.warn("Revisar descensos, valor de origen no se corresponde con la primera fila")

row_1_psi_pou_des=df["psi_POU"].iloc[2]#                                       ¡¡¡¡ Cuidado es el 3 row !!!!
row_1_psi_pz1_des=df["psi_PZ1"].iloc[0]
row_1_psi_pz2_des=df["psi_PZ2"].iloc[0]



des_pou= df["psi_POU"].iloc[3:].apply(lambda x: (x-row_1_psi_pou_des)).values # ¡¡¡¡¡Cuidado la resta empieza  a parir del cuarto row !!!!
v = 3*[v_descenso_origen_pou] #                                             ¡¡¡¡¡Cuidado!!!!
des_pou= np.insert(des_pou, 0, v, axis=0) #                                 ¡¡¡¡¡Cuidado!!!!


v = 3*[v_descenso_origen_pou]

des_pz1= df["psi_PZ1"].iloc[1:].apply(lambda x: (x-row_1_psi_pz1_des)).values
des_pz1= np.insert(des_pz1, 0, v_descenso_origen_pz1, axis=0)


des_pz2= df["psi_PZ2"].iloc[1:].apply(lambda x: (x-row_1_psi_pz2_des)).values
des_pz2= np.insert(des_pz2, 0, v_descenso_origen_pz2, axis=0)

df["des_POU"]=des_pou
df["des_PZ1"]=des_pz1
df["des_PZ2"]=des_pz2


#                                           Profunidades (Fondaria)
row_1_psi_pou_fon=df["des_POU"].iloc[0]#                                        
row_1_psi_pz1_fon=df["des_PZ1"].iloc[0]
row_1_psi_pz2_fon=df["des_PZ2"].iloc[0]


fon_pou= df["des_POU"].iloc[3:].apply(lambda x: (row_1_psi_pou_fon-x)).values # ¡¡¡¡¡Cuidado la resta empieza  a parir del cuarto row !!!!
v = 3*[v_descenso_origen_pou] #                                             ¡¡¡¡¡Cuidado!!!!
fon_pou= np.insert(fon_pou, 0, v, axis=0) #                                 ¡¡¡¡¡Cuidado!!!!

fon_pz1= df["des_PZ1"].iloc[1:].apply(lambda x: (row_1_psi_pz1_fon+x)).values
fon_pz1= np.insert(fon_pz1, 0, v_descenso_origen_pz1, axis=0)


fon_pz2= df["des_PZ2"].iloc[1:].apply(lambda x: (row_1_psi_pz2_fon+x)).values
fon_pz2= np.insert(fon_pz2, 0, v_descenso_origen_pz2, axis=0)

df["fon_POU"]=fon_pou  #                                                      ALERTA EN EL EXCEL --> Duda porque en el excel aparece como que resto y en los demás suma. 
df["fon_PZ1"]=fon_pz1
df["fon_PZ2"]=fon_pz2

#                                        Cotas NP

df["cota_POU"]= df["fon_POU"].apply(lambda x: cota_np_pou- x ) 
df["cota_PZ1"]=df["fon_PZ1"].apply(lambda x: cota_np_pz1- x ) 
df["cota_PZ2"]=df["fon_PZ2"].apply(lambda x: cota_np_pz2- x ) 

print(df.head(5))


df.to_excel("data/resultado.xlsx",sheet_name='Sensores_Pineda')  
t2= time.time()

t_ejecucion= t2-t1

print ("Finalizado en %s"%(t_ejecucion))
