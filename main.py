from bs4 import BeautifulSoup as bs
import requests

url = "https://www.bolsadecereales.com/"

html= requests.get(url)
content= html.content
soup= bs(content, "lxml")

flash= soup.find("table", {"class":"flash active"})


print(flash)
#print(precio) 