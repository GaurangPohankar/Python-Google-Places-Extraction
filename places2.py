from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re
import json
req = Request('https://www.google.com/maps/search/nagpur+hotels/@21.1183457,79.084337,13z/data=!3m1!4b1!4m4!2m3!5m2!5m1!1s2018-09-30', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
avl=['440','425','AEj','Xd','ar','VD','AF1','NxK','AAAAAAAA','photos','google','maps','tactilecsi','wMoA','gMoA','bMYt','Google','Enable','page','null']
soup = BeautifulSoup(webpage, "lxml")

for script in soup(["style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)
links = re.findall(r'(http.*?)"', text)
for link in links:
    text = text.replace(link, '')
#text = re.sub(r'[^\w]', ' ', text)
#text= re.sub(r'\b\w{1,3}\b', '', text)
    
#print( [i for i in re.sub(r'[.,!?]', '', text.lower()).split() if not re.search(r'\d', i)] )

newtext = ""
for word in text.split():
    if not(any(char.isdigit() for char in word) and any(char.isalpha() for char in word)):
        newtext += word + " "

for kar in avl:
    newtext=' '.join([ word for word in newtext.split() if not word.startswith(kar) ])
    
for x in newtext.split():
    if x.isdigit():
        if len(x) > 15:
            newtext = newtext.replace(x, ' ')
    if len(x) > 40:
        newtext = newtext.replace(x, '₹')
        
kvl= str(newtext).split('₹')

print(kvl)
