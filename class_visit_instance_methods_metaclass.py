class O(type):
	def __new__(cls , name , bases , attrs):
		print('===========')
		print(cls)
		print(name)
		print(bases)
		print(attrs)
		print('===========')
		return type.__new__(cls, name, bases, attrs)

	def __getattribute__(self , name):

		if self == A:
			print('attribute')
			return getattr(self(),name)
		else:
			return getattr(self,name)


class A(object , metaclass = O):
	def zhan(self):
		return 'zhan_return'


a = A()

print(a.zhan)
print('-------------')
print(A.zhan())#类不能调用实例方法;通过修改metaclass修改
print('-------------')


class A(object):
	def __setattr__(self,name ,value):
		print(value)
		pass
A.__setattr__(A(),'name','zhanghui')#类调用实例方法,自己给定self实例

