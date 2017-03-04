#Simple Select using BeautifulSoup

import requests
from  bs4 import BeautifulSoup as bs

html=requests.get("http://www.pythonscraping.com/exercises/exercise1.html").text
soup=bs(html,'html.parser')

print soup.h1


