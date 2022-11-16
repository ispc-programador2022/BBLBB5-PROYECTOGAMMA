#Librerias a utilizar
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://bolsadecereales.com/"

pagina = requests.get(url)

soup = BeautifulSoup(pagina.content, "html.parser")



#Cultivos
#Codigo para obtener los nombres de los cultivos
cult = soup.find_all("div", class_="tab flash active")

cultivos = list()

for i in cult:
    cultivos.append(i.text)

flashC= soup.find_all("div", class_="tab flash")

flashList = list()

for i in flashC:
    cultivos.append(i.text)

#print(cultivos) #Impresión de prueba

#-----------OBTENER PRECIO DEL MERCADO DEL TRIGO--------------------

#Debido a que cada etiqueta y clase del cosigo Html repite la etiqueta Td se implementó 
#un bucle para solo obtener la etiqueta que mantiene el precio del valor del mercado
#en todas las etiquetas de cada cultivo siempre es la ultima etiqueta que posee ese valor

box = soup.find("table", class_="flash active", id="flash-trigo")

trig= box.find_all("td")

trigo = list()

for i in trig:
    trigo.append(i.text)

count = 1
for i in trig:
    if count < len(trigo):
        trigo.pop(0)
    elif count == 1:
        break
 
#print(trigo)

#-------OBTENER PRECIO DEL MERCADO DEL MAIZ----------------


box2 = soup.find("table", class_="flash", id="flash-maiz")

maz= box2.find_all("td")

maiz = list()

for i in maz:
    maiz.append(i.text)

count = 1
for i in maz:
    if count < len(maiz):
        maiz.pop(0)
    elif count == 1:
        break
 
#print(maiz)

#--------OBTENER PRECIO DEL MERCADO DE LA SOJA ------------

box3 = soup.find("table", class_="flash", id="flash-soja")

soj= box3.find_all("td")

soja = list()

for i in soj:
    soja.append(i.text)

count = 1
for i in soj:
    if count < len(soja):
        soja.pop(0)
    elif count == 1:
        break
 
#print(soja)

#--------OBTENER PRECIO DEL MERCADO DEL GIRASOL ------------

box4 = soup.find("table", class_="flash", id="flash-girasol")

gir= box4.find_all("td")

girasol = list()

for i in gir:
    girasol.append(i.text)

count = 1
for i in gir:
    if count < len(girasol):
        girasol.pop(0)
    elif count == 1:
        break
 
#print(girasol)

preciosTotales=trigo, maiz, soja, girasol

#print(preciosTotales)

#IMPORTAR ELEMENTOS OBTENIDOS A ARCHIVO .CSV

df = pd.DataFrame({"Cultivos":cultivos, "Precios": preciosTotales}, index= list(range(1,5)))
print('Se imprime los valores obtenidos y luego son guardados en un archivo .csv')
print(df)
print()
df.to_csv("Flash de Cotizaciones.csv", index=True)

#------LEER ARCHIVO .CSV CREADO --------------#
print("Lectura del archivo .csv creado")
datos = pd.read_csv('Flash de Cotizaciones.csv', header=0)
print(datos)