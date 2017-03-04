#Find Descendants
import requests
from bs4 import BeautifulSoup as bs 

html=requests.get("http://www.pythonscraping.com/pages/page3.html")
soup=bs(html.text,"html.parser")
nameList=soup.find("table",{"id":"giftList"})

for x in nameList.children:
	print x
