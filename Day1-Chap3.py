#Select By Attribute
import requests
from bs4 import BeautifulSoup as bs

html=requests.get("http://www.pythonscraping.com/pages/warandpeace.html")
soup=bs(html.text,"html.parser")
#print soup
nameItems=soup.findAll(id="text")
print nameItems[0].text

