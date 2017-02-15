g=(x*x for x in range(10))
#generator 保存的是算法，每次用next（g）调用都会返回下一个值；一般用for
def fib(max):
	n,a,b=0,0,1
	while n<max:
		yield print(b)#每次执行到这里结束，next(g)继续执行；一般用for 
		a,b=b,a+b
		n=n+1
	return 'done'
