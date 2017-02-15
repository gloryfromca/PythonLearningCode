from urllib import request,parse
from enum import Enum,unique 

#和风天气API
class weather(object):
    def __init__(self):
        self.key='382c67628a31410984cb2d859dd58967'
        self.basic_url='https://free-api.heweather.com/v5'
        
    def get_weather(self,city,*key):
        #key限定在suggestion、aqi、now几个数据之间
        # print(type(key))#是一个tuple类型
        weather_url='%s/weather?city=%s&key=%s'%(self.basic_url,city,self.key)
        with request.urlopen(weather_url)  as f:
            a=eval(f.read().decode('utf-8'))
            
        if  len(key)==1:
            a=weather.details1(a,key)
        if  len(key)==2:
            a=weather.details2(a,key)
        if  len(key)==3:
            a=weather.details3(a,key)
        return a
    @staticmethod
    def details1(a,key):
        b=(a['HeWeather5'][0][key[0]])
        return b
    @staticmethod
    def details2(a,key):
        b=(a['HeWeather5'][0][key[0]][key[1]])
        return b
    @staticmethod
    def details3(a,key):
        b=(a['HeWeather5'][0][key[0]][key[1]][key[2]])
        return b

a=weather()
s=a.get_weather('shanghai','now','wind')
s=a.get_weather('shanghai','now')
s=a.get_weather('shanghai')
print(s)
print('------------------')
s=a.get_weather('shanghai','suggestion','air','txt')
print(s)
print('\n')#反斜杠



