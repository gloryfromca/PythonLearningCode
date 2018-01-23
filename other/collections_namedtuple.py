from collections import namedtuple
asd=namedtuple('point',['x','y'])
print(asd)#在函数内部定义的类，所以__main__.point
print(asd.x)
asd.z=0#好像是给类附加了类属性
print(asd.x)
a=asd(1,2)
a=asd(4,5)
print(a.x)#注意输出了0，而不是1
print(a.y)
# a=point(1,2) #error
