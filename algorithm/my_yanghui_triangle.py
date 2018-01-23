def yanghuisanjiao(max):
	if max==1:
		print('1')
		return ('done')
	x=1
	n=1
	a=[1,]
	while n<max+1:#n为第几行，要记住n的实际意义而不是字母
		b=list(range(n))
		b[n-1]=b[0]=1
		while x<n-1:# x 为操作的a中元素的下标的变量，根据杨辉三角定义要求第n行操作到下标为n-2的元素，
					#即x最大为n-2，然后不满足条件，退出循环
			b[x]=a[x]+a[x-1]
			x=x+1
		yield b
		a=b
		x=1
		n=n+1
	return ('done')
	#for n in generator：  中的n没有实际意义，代表执行生成器generator直到迭代过程结束或者冒号下面的条件break
	#必须要在当前目录下才能import函数，负责找不到	