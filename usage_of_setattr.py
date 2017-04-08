
class test(object):
	"""docstring for test"""
	def __init__(self, arg):
		test.__setattr__(test,arg)
		#使用test中的__setattr__方法,而不是self的__setattr__方法
		#使用test不使用self，因为self是test的子类，使用的是子类的__setattr__方法
		#后面的一个test导致最终调用的是test.arg=arg，也就是说最终定义的是test类的属性
	def __setattr__(self,arg):
		print('test的调用方法')
		self.arg = arg

class surname(test):
	# def __init__(self,*arg):
	# 	super(surname, self).__init__(*arg)
	# 	#初始化遇到赋值，自动调用__setattr__方法，该方法中使用了self,也就是初始化完成后形成的实例。
	# 	#所以需要完成初始化。造成了无限的递归调用。
	# 	print('hui')#未打印
	def __setattr__(self,key,value):
		self.key=value
c=surname('zhang')
print(test.arg)
print(surname.arg)
c.arg='zhang'
#报错。已经初始化完成，还是报错，说明无限调用的发生是在使用__setattr__的时候。
#根本原因是__setattr__方法里赋值的形式是默认的self.key=value设置类属性的形式的话，就会报错。



















