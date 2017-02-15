#Iterable & Iterator 可迭代对象和迭代器 注意首字母大写
#Iterable（可迭代对象）includes generator(生成器) and list、tuple、set、str等集合对象
#generator（生成器）includes 使用yield的 functions and  用（）方式生成的
from collections import Iterable
from collections import Iterator
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('abc',Iterable))
print(isinstance((x for x in range(100)),Iterable))
print(isinstance(100,Iterable))
print('-----------------------------')
#from collections import Iterator
print(isinstance([],Iterator))
print(isinstance({},Iterator))
print(isinstance('abc',Iterator))
print(isinstance((x for x in range(100)),Iterator))
print(isinstance(100,Iterator))
a=[1,2,3,4,7]
print ([x for x in a]) #打印一个list
print (x for x in a )#打印一个generator object的地址
for n in (x for x in a):
	print (n)
#print(x) for x in a，for的前面不能用print处理数据,只能将整体for in 结构作为print的对象
#如果for in 循环语句后面用：表示下面为操作步骤的话，则for前面不能加东西；
#如果for前面加东西说明要么是为了获得一个生成器，要么打算将结果放在一个list中


#Python的for循环本质上就是通过不断调用next()函数实现的

a=iter(a)
#iter(a) 不行，因为赋值给变量才能创建
#a.iter() 不行，这种写法也改不了a


while True:#Ture 首字母要大写
	try:
		x=next(a)	
	except StopIteration:
		break
def num():
	n=0
	while True:
		yield(n)
		n=n+1


#从test导入函数，会先把上面的执行一遍，可以尝试一下导入num（）函数.


#print num 返回 functions id ; print num() 返回 generator object id.


#next(num())和g=num()、next(g)不同，前者是一个迭代器对象，next()调用相当于每次重新调用函数；
#后者g=num()则创建了一个迭代器对象并指向变量g，每次next(g)都是在变量g中进行;
#可以分别实验一下效果，并打印id.




#生成器对象（generator object）包含了函数的原始代码和函数调用的状态，
#这状态包括函数中变量值以及当前的执行点——函数在yield语句处暂停（suspended），
#返回当前的值并储存函数的调用状态，当需要下一个条目（item）时，可以再次调用next，
#从函数上次停止的状态继续执行，知道下一个yield语句.
