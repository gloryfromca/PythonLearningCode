
class surname(object):
	def __init__(self):
		self._name = {} 

	@property#既能检查参数，又可以用类似属性这样简单的方式来访问类的变量
	def name(self):
		return self._name
	@name.setter
	def name(self,value):
		if value not in ('zhang',"jiang"):
			raise ValueError('我不姓<%s>'%value)
		self._name=value
s=surname()
print(type(s.name))#<class 'dict'>
s.name='zhang'
print(s.name)
s.name='jiang'
print(s.name)


















