from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://www.python.org/events/python-events/')
content = BeautifulSoup(html,'lxml')#content就像一个有目录索引的文本内容
didian = content.findAll('span',{'class':'event-location'})
shijian = content.findAll('time')
title = content.findAll('h3',{'class':'event-title'})
print(content.name)
print(type(content))
# print(didian.name)#error
print(didian[0].name)#结果是span
print(didian[0].attrs)#结果是attrs
print(type(didian))
print(type(didian[1]))
print('------------------')
for z in range(len(didian)):
    print(didian[z].get_text(),shijian[z].get_text(),title[z].get_text())
    # print('地点:%s 时间:%s 主题:%s'% (x.get_text(),y.attrs['datetime'],z.get_text()))
