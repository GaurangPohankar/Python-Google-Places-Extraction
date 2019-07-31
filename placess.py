from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re
import json

req = Request('https://www.google.com/maps/search/nagpur+hotels/@21.1183457,79.084337,13z/data=!3m1!4b1!4m4!2m3!5m2!5m1!1s2018-09-30', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, "html.parser")

mydivs = soup.find("div", class_="gm2-caption")
print(mydivs)
