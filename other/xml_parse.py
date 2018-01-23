from urllib import request
import base64
import urllib
from xml.parsers.expat import ParserCreate
all_mes=[]

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        # if 'tomorrow' in weather:
        #     return
        #没用上但是很有用
        if name=='yweather:location':
            a={'city':attrs['city'],'country':attrs['country']}
            all_mes.append(a)
            print(type(attrs))
        if name=='yweather:forecast':
            a={'text':attrs['text'],'low':attrs['low'],'high':attrs['high']}
            all_mes.append(a)
            print(type(attrs))

    def end_element(self, name):
        pass
        # print('sax:end_element: %s' % name)

    def char_data(self, text):
        pass
        # print('sax:char_data: %s' % text)


xml=r'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<rss version="2.0" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
    <channel>
        <title>Yahoo! Weather - Beijing, CN</title>
        <lastBuildDate>Wed, 27 May 2015 11:00 am CST</lastBuildDate>
        <yweather:location city="Beijing" region="" country="China"/>
        <yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
        <yweather:wind chill="28" direction="180" speed="14.48" />
        <yweather:atmosphere humidity="53" visibility="2.61" pressure="1006.1" rising="0" />
        <yweather:astronomy sunrise="4:51 am" sunset="7:32 pm"/>
        <item>
            <geo:lat>39.91</geo:lat>
            <geo:long>116.39</geo:long>
            <pubDate>Wed, 27 May 2015 11:00 am CST</pubDate>
            <yweather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" />
            <yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
            <yweather:forecast day="Thu" date="28 May 2015" low="21" high="34" text="Sunny" code="32" />
            <yweather:forecast day="Fri" date="29 May 2015" low="18" high="25" text="AM Showers" code="39" />
            <yweather:forecast day="Sat" date="30 May 2015" low="18" high="32" text="Sunny" code="32" />
            <yweather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" />
        </item>
    </channel>
</rss>
'''
def parse_weather(xml):
    handler = DefaultSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml)
    print(all_mes[0])    
    print(all_mes[1])
if __name__=="__main__":
    with request.urlopen('http://blog.sina.com.cn/s/blog_7648f7170100qcdz.html') as f:
        ssr=f.read().decode('utf-8')
        
    print(ssr)
    print('-------------')
    parse_weather(xml)
    # parse_weather(ssr)
    # print(type(ssr))
    # print(ssr)