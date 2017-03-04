#Find Parents
import requests
from bs4 import BeautifulSoup as bs

html=requests.get("http://www.pythonscraping.com/pages/page3.html").text
soup=bs(html,"html.parser")
nametags=soup.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text()
print nametags
