import urllib.request
from bs4 import BeautifulSoup

response = urllib.request.urlopen('http://python.org')
html=response.read()

soup=BeautifulSoup(html,"html.parser")

a_tags=soup('a')

for rows in a_tags:
    print(rows)

print(response.info())
#for line in html:
#    print(line)
