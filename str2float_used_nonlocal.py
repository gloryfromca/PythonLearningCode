#第一次调用function时，如果提供initial参数，会以sequence中的第一个元素和initial作为参数调用function，
#否则会以序列sequence中的前两个元素做参数调用function。reduce(lambda x, y: x + y, [2, 3, 4, 5, 6], 1)
from functools import reduce
def str2float(s):
	char_to_float={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'.':-1}
	nums=map(lambda ch:char_to_float[ch],s)
	point=0
	def tofloat(a,b):
		nonlocal point #引用外层变量，使得函数内部的操作能够改变上一层结构中的变量
		if b==-1:
			point=1
			return a
		elif point==0:
				return a*10+b#多缩进没关系，但是内部的一定要相比主体缩进
		else:
				point=point*10
				return a+b/point
	return reduce(tofloat,nums,0) #reduce 一直接收两个参数
