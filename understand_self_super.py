class A:
  def m(self):
    print('A')

class B(A):
  def m(self):
    print('B')
    super().m()
class C(B):
  def m(self):
    print('C')
    # see the difference!
    print(__class__.__mro__)
    print(__class__.__name__)#预期是C
    #print(__class__.test)
    print(__class__.__class__.__mro__)
    print(self.__class__.__mro__)
    __class__.__mro__[2].m(self)#记得要写参数self。
  def test(self):
    print('__class__就是本类的')

class D(C):
  def m(self):
    print('D')
    super().m()
o = D()
g=C()
g.m()
print('-------------------------')
o.m()#其实就是把o对象执行其对应类的方法
print('-------------------------')
D.m(o)#上下两个意思完全一样
print('-------------------------')
#D.m() 没有这种表达 