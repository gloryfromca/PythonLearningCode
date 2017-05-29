class Meter(object):
    '''米的描述符。'''

    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
            self.value = float(value)

class Foot(object):
    '''英尺的描述符。'''

    def __get__(self, instance, owner):
            return instance.meter * 3.2808
    def __set__(self, instance, value):
            instance.meter = float(value) / 3.2808

class Distance(object):
    '''用于描述距离的类，包含英尺和米两个描述符。'''
    meter = Meter()
    foot = Foot()

c = Distance() 
c.meter = 3
print(c.foot)


print('============')

class A(object):
    name = 'zhanghui_A'
class B(A):
    pass
a = A()
a.name = 'zhanghui_change'
print(a.name)

print('============')

class A(object):
    def __get__(self , instance , owner):
        return 'A'
    def __set__(self , instance ,value):
        self.value = value
class B(object):
    a_attr = A()

b = B()
b.a_attr = 'new_set'
print(b.a_attr)

#数据描述器大于实例属性

print('============')

class A(object):
    def __get__(self , instance , owner):
        return 'A'
    # def __set__(self , instance ,value):
    #     self.value = value
class B(object):
    a_attr = A()

b = B()
b.a_attr = 'new_set'
print(b.a_attr)

#实例属性大于非数据描述器

print('============')

class S(object):
    pass

class B(object):
    a_attr = A()
    def __setattr__(self , name , value):
        setattr(S,name ,value)
        print("pass A_setattr")

b = B()
b.a_attr = 'new_set'
print(b.a_attr)
print(S.a_attr)

print('============')

class SS(object):
    def __get__(self , instance ,owner):
        return 'sss'
class D(object):
    d =SS()
    def __init__(self):
        self.d = SS()

dd = D()
print(dd.d)#访问到了实例属性；实例属性不调用描述器的__get__方法；指向的是实例对象
print(D.d)#访问到了描述器，调用了Descr.__get__(attr, a, A)方法

print('============')


class Descriptor(object):
    def __get__(self, instance, owner):
        print("get", "self:", self, "instance", instance, "owner", owner)
        return 'test'

    def __set__(self, instance, value):
        print("set", "self:", self, "instance", instance, "value", value)

    def __delete__(self, instance):
        print("del", "self:", self)

    def __del__(self):#莫名其妙地调用，可能是旧式类的调用方式
        print("del", "self:", self)



class Foo(object):
    x = Descriptor()

    def __init__(self, x):
        # x这个属性由Descriptor类代理
        self.x = x #Foo类中的__setattr__的内建方法起作用

    def __setattr__(self, name, value):
        print("ss")
        return 'sss'

foo = Foo(10)
print('---------------')
print(foo.x)


