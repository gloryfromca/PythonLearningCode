
class surname(dict):
	def __init__(self):
		self._name = {} 
	def __getattr__(self,key):
		return '没有%s属性'%key
c=surname()
print(c.ss)





















