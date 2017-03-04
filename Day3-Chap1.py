#Print datetime
#Get all the wiki links from /wiki/Kevin_Bacon   http://en.wikipedia.org and for each and every link get the particular wiki link

import datetime as dt 
import requests
from bs4 import BeautifulSoup as bs
import re
print dt.datetime.now()
import random

def getlinks(actionUrl):

	html=requests.get("http://en.wikipedia.org"+actionUrl).text
	#print html
	soup=bs(html,"html.parser")
	anchortags=soup.findAll('a',href=re.compile("^(/wiki/)[A-Za-z]*$"))
	return anchortags

links=getlinks("/wiki/Kevin_Bacon")

while len(links)>0:
	newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
	print newArticle
	links = getlinks(newArticle)