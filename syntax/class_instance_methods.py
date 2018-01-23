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
		return getattr(self(),name)



class A(object , metaclass = O):
	def zhan(self):
		print('zhan')


a = A()

print(a.zhan)
print(A.zhan())#类不能调用实例方法

