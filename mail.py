#------------- importo las librerias  -------------#
from bs4 import BeautifulSoup as bs
import requests 
import pandas as pd
import os.path as path


#------------- cargo las variables y utilizo request         -------------#
#------------- para armar en content la estructura del HTML  -------------#
#------------- luego completo la sopa con lxml               -------------#
url = "https://www.bolsadecereales.com/"
html= requests.get(url)
content= html.content
soup= bs(content, "lxml")

#------------- nombro las listas vacias para cada cereal -------------#

#------------- listas de los cotizadores vacios -------------#
titulos_trigo   = []
titulos_maiz    = []
titulos_girasol = []
titulos_soja    = []

#------------- listas de las fechas cotizadas vacios-------------#
fechas_trigo    = []
fechas_maiz     = []
fechas_girasol  = []
fechas_soja     = []

#------------- listas de los valores cotizados vacios-------------#
datas_trigo     = []
datas_maiz      = []
datas_girasol   = []
datas_soja      = []

#------------- busco en el HTML las tablas con el   -------------#
#------------- atributo de id: flash-trigo que es generica  -------------#
table_trigo= soup.find("table", attrs={'id':'flash-trigo'})
#------------- cargo el cuerpo de la tabla   -------------#
table_body_trigo = table_trigo.find('tbody')
#------------- cargo los registros   -------------#
rows = table_body_trigo.find_all('tr')
trigo_lista = list()
#------------- para cada registro tomo las columnas   -------------#
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    #------------- para cada columna del registro tomo el valor que tenga mas de una columna -------------#
    #------------- ya que en la estructura existen a modo de titulo algunos valores inecesarios -------------#
    if len(cols) > 1:
      titulos_trigo.append(cols[0])
      fechas_trigo.append(cols[1])
      datas_trigo.append(cols[3])

    #------------- realizo lo mismo para los demas cereales -------------#
table_maiz= soup.find("table", attrs={'id':'flash-maiz'})
table_body_maiz = table_maiz.find('tbody')
rows = table_body_maiz.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    if len(cols) > 1:
      titulos_maiz.append(cols[0])        
      fechas_maiz.append(cols[1])
      datas_maiz.append(cols[3])
#------------- realizo lo mismo para los demas cereales -------------#
table_soja= soup.find("table", attrs={'id':'flash-soja'})
table_body_soja = table_soja.find('tbody')
rows = table_body_soja.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    if len(cols) > 1:
      titulos_soja.append(cols[0])        
      fechas_soja.append(cols[1])
      datas_soja.append(cols[3])
#------------- realizo lo mismo para los demas cereales -------------#
table_girasol= soup.find("table", attrs={'id':'flash-girasol'})
table_body_girasol = table_girasol.find('tbody')
rows = table_body_girasol.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    if len(cols) > 1:
      titulos_girasol.append(cols[0])        
      fechas_girasol.append(cols[1])
      datas_girasol.append(cols[3])
#------------- defino las listas vacias de cada valor  -------------#
titulo = []
precio = []
fecha  = []
cereal = []
#------------- acomodo una sola lista que incluya todos los cereales con sus  -------------#
#------------- respectivos valores  -------------#
################################
# Trigo
################################
for titulo_trigo in titulos_trigo:
  titulo.append(titulo_trigo)
  cereal.append("Trigo")
for fecha_trigo in fechas_trigo:
  fecha.append(fecha_trigo)
for data_trigo in datas_trigo:
  precio.append(data_trigo)
################################
# Maiz
################################
for titulo_maiz in titulos_maiz:
  titulo.append(titulo_maiz)
  cereal.append("Maiz")
for fecha_maiz in fechas_maiz:
  fecha.append(fecha_maiz)
for data_maiz in datas_maiz:
  precio.append(data_maiz)
################################
# Soja
################################
for titulo_soja in titulos_soja:
  titulo.append(titulo_soja)
  cereal.append("Soja")
for fecha_soja in fechas_soja:
  fecha.append(fecha_soja)
for data_soja in datas_soja:
  precio.append(data_soja)
################################
# Girasol
################################
for titulo_girasol in titulos_girasol:
  titulo.append(titulo_girasol)
  cereal.append("Girasol")
for fecha_girasol in fechas_girasol:
  fecha.append(fecha_girasol)
for data_girasol in datas_girasol:
  precio.append(data_girasol)

#verifico que exista el archivo a guardar
if path.exists("Flash_de_Cotizaciones.csv"):
  #si existe lo leo
  data_Frame_archivo = pd.read_csv("Flash_de_Cotizaciones.csv")
  #verifico que no exista en el mismo una fecha a insertar
  if fecha[0] not in data_Frame_archivo.values:
    #si no existe esa fecha entonces agrego los nuevos registros
    nueva_fila = pd.DataFrame({"Cereal":cereal,"Origen": titulo, "Fecha":fecha, "Precios":precio})
    df = data_Frame_archivo.append(nueva_fila, ignore_index=True )
    df.to_csv("Flash_de_Cotizaciones.csv", index=False)
else:
  #si no existe existe el archivo creo un nuevo DataFrame
  df = pd.DataFrame({"Cereal":cereal,"Origen": titulo, "Fecha":fecha, "Precios":precio})
  df.to_csv("Flash_de_Cotizaciones.csv", index=False)

#------------  leo el nuevo archivo y lo imprimo en consola  -------------#
datos = pd.read_csv('Flash_de_Cotizaciones.csv', header=0)
print (datos)