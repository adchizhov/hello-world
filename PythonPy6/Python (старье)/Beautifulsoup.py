import urllib.request as urreq
from bs4 import BeautifulSoup

url=input('Enter - ')
html=urreq.urlopen(url)
soup=BeautifulSoup(html, "html.parser")
tags=soup('a')
for tag in tags:
    print (tag.get('href', None))
