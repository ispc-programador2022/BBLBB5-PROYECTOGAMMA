from bs4 import BeautifulSoup as bs
import requests 

url = "https://www.bolsadecereales.com/"
html= requests.get(url)
content= html.content
soup= bs(content, "lxml")

data_trigo = []
data_maiz = []
data_girasol = []
data_soja = []

table_trigo= soup.find("table", attrs={'id':'flash-trigo'})
table_body_trigo = table_trigo.find('tbody')
rows = table_body_trigo.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data_trigo.append([ele for ele in cols if ele])

table_maiz= soup.find("table", attrs={'id':'flash-maiz'})
table_body_maiz = table_maiz.find('tbody')
rows = table_body_maiz.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data_maiz.append([ele for ele in cols if ele])

table_soja= soup.find("table", attrs={'id':'flash-soja'})
table_body_soja = table_soja.find('tbody')
rows = table_body_soja.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data_soja.append([ele for ele in cols if ele])

table_girasol= soup.find("table", attrs={'id':'flash-girasol'})
table_body_girasol = table_girasol.find('tbody')
rows = table_body_girasol.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data_girasol.append([ele for ele in cols if ele])


print ('Trigo')
print (data_trigo)
print ('Maiz')
print (data_maiz)
print ('Soja')
print (data_soja)
print ('Girasol')
print (data_girasol)
