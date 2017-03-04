#Get all the image source
import requests
from bs4 import BeautifulSoup as bs
import re

html = requests.get("http://www.pythonscraping.com/pages/page3.html").text
soup=bs(html,"html.parser")
images=soup.findAll("img",{"src":re.compile("\w+.jpg")})
for image in images: 
    print image["src"]