#函数本身也可以赋值给变量，即：变量可以指向函数
#函数名其实就是指向函数的变量,把abs指向10后，就无法通过abs(-10)调用该函数,因为abs指向整数10
#把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式
from functools import reduce
def str2int(s):
	def  fn(x,y):	
		return x*10+y	
	def  char2nums(s):
		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]#定义一个字典k，k[s]返回key对应的value
	it=reduce(fn,map(char2nums,s))
	
	#map()函数接收两个参数，一个是函数，一个是Iterable，
	#map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

	#map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，
	#Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
	print(reduce(fn,map(char2nums,s)))
	print(it)
	