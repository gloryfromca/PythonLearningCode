a=1
aa=1
print(a)
print(id(a))
print(id(aa))
#aa指向的变量和a指向的对象相同，都是不可变的对象int类型的1 ，python不会创建新的对象，
#而是让二者变量指向同一个内存地址，如果修改一个变量的值，就更改这个变量地址中的指向地址
a+=1
print(id(a))
#变量a重新赋值，则为新的值创建内存地址并让变量指向新的内存地址，
#旧对象不改变，如果没有别的变量指向旧的对象，等待回收
print('--------------------------')


b=[1,2,3]
bb=[1,2,3]
bbb=b
print(id(b))
print(id(bb))#list可变，应赋予不同的地址，否则会造成对新变量的操作改变原来的变量
print(id(bbb))
print([id(x) for x in b])
print([id(x) for x in bb])
print([id(x) for x in bbb])
b[1]=85
print(b)
print(id(b))
#list本身地址不变，但是list中储存的第二个元素的地址变掉了
#（list可变指的是list地址不会变，不会创建新的对象，而是地址指向的内容变掉了）
print([id(x) for x in b])
print([id(x) for x in bb])
print([id(x) for x in bbb])

b[1]=2
print(b)
print(id(b))
#为什么都没有变呢？因为b[1]本身就等于2，所以list中三个对象引用（内存地址）都没有变
print([id(x) for x in b])
print([id(x) for x in bb])
print([id(x) for x in bbb])

from copy import deepcopy
bbbb=deepcopy(b)
print(id(bbbb))
b[0]=65
print(b)
print(id(b))
print([id(x) for x in b])
#可以理解为代码中的变量赋值创建后会将变量和一个内存地址（id）挂钩，重新复制即改挂钩
#list的地址中会存放所有对象的引用（元素的内存地址），可以更改该引用
#常规复制只是浅拷贝，将容器内元素的地址复制一份到新的容器（新的变量）
#deepcopy是深拷贝，容器中的元素都会重新创建内存地址放置
print('--------------------------')
c=(1,2,3)
print(c)
print(id(c))
print([id(x) for x in c])

cc=c 
print(cc)
print(id(cc))
print([id(x) for x in cc])
#tuple不可变，变量cc不需要新的地址，而是指向c的地址.更改cc即更改变量cc指向的地址

cc=(12,2,3)
print(cc)
print(id(cc))
print([id(x) for x in cc])

ccc=(1,2,3)
print(ccc)
print(id(ccc))
print([id(x) for x in ccc])
#改变c
print('--------------------------')
e=[1,2,3]
d=(1,2,3,e)
print(d)
print(d[3][1])
print(id(d))
print([id(x) for x in d])
e[1]=14
print(d[3][1])
print([id(x) for x in d])
#貌似“可变“的tuple

print('--------------------------')
#c[0]=13
#print(c)
#print(id(c))
#说明tuple变量地址中的对象引用不能改；list变量地址中的对象引用可以改

f=set([1,2,3,3])
print(f)
print(id(f))
print([id(x) for x in f])

