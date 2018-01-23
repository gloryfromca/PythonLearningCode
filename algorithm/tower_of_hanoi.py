def move(n,a,b,c): # a变量是要求的移动tower of hanoi 的原位置，c变量是移动的terminal，b变量是中转站	
	if n==1: #双等号被认为是判断，单等号是赋值
		print(a,'-->',c)#不能认为是print(‘A-->C’)可以等价替换
		return 
	move(n-1,a,c,b)#实现将n-1阶的tower of hanoi从n阶汉诺塔的出发点搬到中转站，为第n阶搬到terminal腾出空间,
				   #未实现这一目的可以借用n阶hanoi的terminal.
	print(a,'-->',c)
	move(n-1,b,a,c)

