import urllib
from xml.parsers.expat import ParserCreate
from urllib import request
baseurl = "https://query.yahooapis.com/v1/public/yql?"
yql_query = "select wind from weather.forecast where woeid=2460281"
# yql_query = "select wind  weather.forecast where woeid=2460281"#error，格式不对
yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=xml"
print(yql_url)#注意看URL格式
print('--------------------')

result = urllib.request.urlopen(yql_url).read()
print(result)
a=result.decode('utf-8')
print('--------------------')
print(type(a))
print('--------------------')

print(a)
print('--------------------')

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        # print('sax:end_element: %s' % name)
        pass
    def char_data(self, text):
        # print('sax:char_data: %s' % text)
        pass
handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(a)