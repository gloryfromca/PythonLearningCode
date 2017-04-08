# __setattr__ #设置变量时，该方法自动调用,类必须继承dict; 
class surname(object):
	def __init__(self):
		self._name = 'zhang'
		#初始化遇到赋值，自动调用__setattr__方法，该方法中使用了self,也就是初始化完成后形成的实例。
		#所以需要完成初始化。造成了无限的递归调用。
		print('hui')#未打印
	def __setattr__(self,key,value):
		print("zhang")
		self.key=value
		print('jiang')#未打印
c=surname()
c=surname()




















