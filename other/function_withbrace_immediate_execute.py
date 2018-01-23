def fun():
	print ('middle site')
def prit(fun):
	print('begin ():' )
	result = fun()
	#result= fun 函数加括号会立刻执行
	print('end   ():')
	return result
prit(fun)