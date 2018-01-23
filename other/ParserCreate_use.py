from xml.parsers.expat import ParserCreate
class defaultsaxhandler(object):
	def start_element(self,name,attrs):
		print('start_element:%s,attrs:%s'%(name,str(attrs)))
		# print(type(attrs))
		# print('start_element:%s,attrs:%s'%(name,attrs))
	def end_element(self,name):
		print('end_element:%s'% name)
	def char_data(self,text):
		print('char_data:%s'% text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''
xml1= r'''<?xml version="1.0"?>
<ol><li><a href="/python">Python</a></li><li><a href="/ruby">Ruby</a></li></ol>
'''
handler=defaultsaxhandler()
print(type(defaultsaxhandler))
parser=ParserCreate()#创建解释器
print(type(parser))
print('---------------------------')
parser.StartElementHandler=handler.start_element
parser.EndElementHandler=handler.end_element
parser.CharacterDataHandler=handler.char_data#CharacterDataHandler是parser内部定义的
# parser.Parse(xml)#好像每次只能parser一个；注意看一下，好像char_Data会解析处文档中间的空格
print('------------------')
parser.Parse(xml1)

