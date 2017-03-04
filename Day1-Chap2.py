#Select By Class

import requests
from bs4 import BeautifulSoup as bs


html=requests.get("http://www.pythonscraping.com/pages/warandpeace.html").text
soup=bs(html,"html.parser")
nameLists=soup.findAll("span",{"class":"green"})

for x in nameLists:
	print x.get_text()
