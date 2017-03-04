#Find Siblings
import requests
from bs4 import BeautifulSoup as bs

html=requests.get("http://www.pythonscraping.com/pages/page3.html").text
soup=bs(html,"html.parser")
nametags=soup.find("table",{"id":"giftList"}).tr.next_siblings
for x in nametags:
	print x
