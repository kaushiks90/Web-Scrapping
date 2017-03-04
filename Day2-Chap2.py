#Find all the tags which is having attribute equals to 2
import requests
from bs4 import BeautifulSoup as bs
html = requests.get("http://www.pythonscraping.com/pages/page2.html").text
#print html
soup = bs(html, "html.parser")
tags=soup.findAll(lambda x:len(x.attrs)==2)
for tag in tags:
	print(tag)