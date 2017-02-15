from functools import reduce
def normalize(name_list):
	def initial_upwrite(s):
		return s.capitalize()
	return map(initial_upwrite,name_list) 
#map:一个list作为输入，函数作用于每一个值，并把结果作为一个iterable（可迭代对象，此处是list）返回
#分别尝试normalize（'oisoHH'）、 normalize(['oisoHH',]) 看result

def prod(numbers): #有时候import不进去，exit()然后试一下
	def chengfa(x,y):
		return x*y
	return reduce(chengfa,numbers)

def str2float(str_float):
	g=[{'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[x] for x in str_float if not(x=='.')]
	h=reduce(lambda x,y:10*x+y,g)
	print (g)
	print (h)
	print (enumerate(g))
	p=[i for i,j in enumerate(str_float)if(j=='.')]#之前通不过是因为用了去掉点号的str_float
								#还有就是__for__in___的结构返回的是生成器或者加[]成为list
								#还可以用while结构中累加直到出现‘.’的方式确定元素的index
	print (p) # print 后面的内容必须要用（）括住才行
	
	return h/(10*(len(str_float)-1-int(p[0]))) #后面不是一个等式，而是一个计算式（不能出现等号）
	
