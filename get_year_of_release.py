from bs4 import BeautifulSoup
import requests
import re

link = 'https://ru.wikipedia.org/wiki/Madden_NFL_2004'

html = requests.get(link).text

print(html)
'''
session = requests.session()    
req = session.get()    
doc = BeautifulSoup(req.content)
print(doc.get_text())
#print(doc.prettify())
'''