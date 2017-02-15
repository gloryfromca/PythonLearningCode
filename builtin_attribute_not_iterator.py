mappings={'a':123,'we':"loss"}
class a():
    #ss=mappings
    ss={'as':123,'we':"loss"}
b=a()
print(a.ss)
print(b.ss)
print(b.ss.items())
for k,v in b.ss.items():
    print(k,v)
print('---------循环的分界线---------')
for k,v in b.ss:
    print(k,v)
#内建的函数或者方法不是可迭代对象,必须使用items(),使属性或者方法变成一个可迭代的对象