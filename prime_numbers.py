point=1
k=3
def prime_number1(n):#输出前n个素数,至少n为1
	list_sushu=[2,]
	def judgement(k):
		for x in list_sushu:
			if k%x==0:
				return 0
		return 1
	
	while  point<n:
		global k	  #在函数sushu()外，已经声明了全局变量，这里用global表示内部使用全局变量
		global point  #while循环变量的作用域是模块作用域，而不是单独的作用域。
		if judgement(k)==1:
			point=point+1
			list_sushu.append(k)
			k=k+1
		else:
			k=k+1
	print(k)
	print(point)
	print(list_sushu)
def prime_number2(n):#返回前n个数中的素数
	if n<3:
		return listsushu
	listsushu=[2,]

	def judgement(x):
		nonlocal listsushu
		for n in listsushu: 
			if x%n==0 :
				return 0
		listsushu.append(x)#上下顺序反了
		print(listsushu)
		return 1
		
	print(listsushu) #只是执行了第一次
	print(filter(judgement,range(n)[3:]))#少了一个），一直报unexpected EOF while parsing错误
	print(filter(judgement,range(n)[3:]))
	print([2,]+list(filter(judgement,range(n)[3:])))#惰性序列，不加[]，不返回value,feedback a object index
	print(filter(judgement,[x for x in range(n)]))#列表生成器加[],显示list
	#print(k) 不说明global 变量，则在sushu2()模块的namespace中没有k，point
	#print(point)
print(k)
print(point)

