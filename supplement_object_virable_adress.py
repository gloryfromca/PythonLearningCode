import copy
s=[1,2,3,4]
b=[1,2,3]
print(id(s))
print(id(b))
print(id(s[0]))
print(id(b[0]))
s=-6
a=-6
print(id(s))
print(id(a))#非常驻的数字，二者的地址不同#常驻内存的整数的范围是-5 ~ 99
b=-5
c=-5
print(id(b))
print(id(c))
a=[1,2,3]
print(id(a))#list可变对象，因此可以改变数值而不改变地址
a.append(5)
print(id(a))
print('--------------------')
class b():

    x = []
    def set(self):
        self.x.append(1)
    def get(self):
        return self.x

for i in range(3):
    a = b()
    print(dir(a))
    print(a.__dict__)
    print(a.set())
    print(a.get())
    
print('--------------------')
class b():
    def __init__(self):
        self.x = []
    def set(self):
        self.x.append(1)
    def get(self):
        return self.x

for i in range(3):
    a = b()
    print(dir(a))
    print(a.__dict__)
    print(a.set())
    print(a.get())
print('--------------------')
s=[1,2]
print(id(s))
s=[]
print(id(s))#重新赋值后，s存储的内存地址会重新指向新的内存部分
print('--------------------')
s=[1,2,-6,[3,4],[3,[3,4]]]
d=copy.copy(s)#相当于复制了对象，但是对象中的元素还是共享（python的节约原则）
print(id(s))
print(id(d))
print(id(s[1]))#id不同，但是指向的对象相同
print(id(s[1]))
print(id(s[2]))#id不同，但是指向的对象相同(对象是-6)
print(id(d[2]))
d.append(5)
print(s)
print(d)
d[3][0]=19
print(s)
print(d)#浅拷贝，下标为3的元素是个list，是共享的，因此修改之后s、d都有所反映
print('--------------------')

s=[1,2,-6,[3,4],[3,[3,4]]]
d=copy.deepcopy(s)#相当于复制了对象，但是对象中的元素还是共享（python的节约原则）
print(id(s))
print(id(d))
print(id(s[1]))#id不同，但是指向的对象相同
print(id(s[1]))
print(id(s[3]))#id不同，指向的对象也不同(对象是[3,4])
print(id(d[3]))
print(id(s[4][1]))#可变元素的可变元素也被复制过来，深拷贝！！！！！！
print(id(d[4][1]))
d.append(5)
print(s)
print(d)
d[3][0]=19
print(s)
print(d)#浅拷贝，下标为3的元素是个list，是共享的，因此修改之后s、d都有所反映
print('-----------------')
s1=set([1,2,3])
# s1=set(1,2,3)#传入一个list,或者tuple对象
s2=set([1,2,(3,4)])
# s3=set([1,2,[3,4]])#set中的元素都要可以哈希
# s4=set([1,2,(3,[4,5])])


