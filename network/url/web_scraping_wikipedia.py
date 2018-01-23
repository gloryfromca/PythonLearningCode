from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
from math import  log
random.seed(datetime.datetime.now())
def getlink(url):
    html = urlopen("http://en.wikipedia.org"+url)
    s = BeautifulSoup(html)
    return  s.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))
links = getlink("/wiki/Kevin_Bacon")
n=0
i=1
a=20#=跳转次数+1
while len(links)>0 and i<a:
    newarticle=links[random.randint(0,len(links)-1)].attrs['href']
    print(newarticle)
    n=n+len(links)
    i=i+1
    links = getlink(newarticle)
s=log(5334395)/log(n/(a-1))
print(s)


    