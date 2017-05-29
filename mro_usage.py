class A(object):
	pass
class B(object):
	pass
class C(A):
	pass
class D(C,B):
	pass
print(D.__mro__)
#继承链包括自己