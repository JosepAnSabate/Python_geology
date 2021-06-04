from pathlib import Path
#exemples
#carga datos 
filePath = r'C:\Users\34639\Desktop\pyqgis\u4\ej1_datos\ej2\poi.shp'
shpLayer = QgsVectorLayer(filePath,'capa ejemplo','ogr')
#cargar datos interfaz
#vectorLayer = iface.addVectorLayer(filePath,'capa ejemplo','ogr')

#guardar projecte
#fileName = r'C:\Users\34639\Desktop\pyqgis\u4\ej1_datos\ej2\proyecto.qgs'
#fileSave

#ex1
csv=r'C:\Users\34639\Desktop\pyqgis\u4\ej1_datos\datos_accidentes.csv'
config = '?encoding=windows-1252&type=csv&delimiter=;'
uri = Path(csv).as_uri() + config
shp = r'C:\Users\34639\Desktop\pyqgis\u4\ej1_datos\provincias.shp'

provincias = QgsVectorLayer(shp, 'provincias', 'ogr')
datos = QgsVectorLayer(uri, 'datos_accidentes', 'delimitedtext')

# inspeccionar los datos
csvFieldsNames = datos.fields().names()
print(csvFieldsNames)
csvFeats = datos.getFeatures()

for f in csvFeats:
    data =[]
    for fn in csvFieldsNames:
        data.append(f[fn])
    print(data)

shpFieldsNames = provincias.fields().names()
print(shpFieldsNames)
shpFeats = provincias.getFeatures()

for f in shpFeats:
    data = []
    for fn in shpFieldsNames:
        data.append(f[fn])
    print(data)

#agregar a la capa províncies los campos que nos interesen
 
provincias.startEditing()

for c in csvFieldsNames[0]:
    campo = QgsField(c, QVariant.Int)
    provincias.addAtributte(campo)

provincias.commitChanges()

#inspeccionem els camps afegits a la capa
print(provincias.fields().names())

provincias.startEditing()

#ahoraiteramos sobre las entidades y  vamos rellenando los campos
for f in provincias.getFeatures():
    fid = f.id()
    id_prov = f['id_prov']
    filtro = '"cod" = \'{}\''.format(id_prov)
    dato = datos.getFeatures(filtro)
    for  elem in dato:
        attrs = {}
        for k, fn in enumerate(csvFieldsNames[0:]):
            ind = k + 4
            attrs[ind] = elem[fn]
        #los atributos tienen los indices de la capa destino 
        print(attrs)
    provincias.changeAttributeValues(fid, attrs)
    
#remitimos los cambios a  la capa
provincias.commitChanges()

#visualizar la capa qgis
QgsProject.instance().addMapLayer(provincias)

#ej 2


#obtener los datos i explorar los datos
layer = iface.activeLayer()
layer.fields().names()
layer.sourceCrs().authid()

feat = QgsFeature(layer.fields())
feat.setAttribute(1, "Caleta Hotel")
featGeometry(QgsPoint(36.137206, -5.340712))

#agregamos la entidad a la capa
layer.startEditing()
layer.addFeature(feat)
layer.commitChanges()
















