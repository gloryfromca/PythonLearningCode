def my_abs(x):
	if not isinstance(x,(int,float)):
		raise typeerror('兄弟，你数据类型错了！')
	if x>0:	
		pass
	else :
		x=-x
	return x
#必须注意函数的部分缩进，return部分不能和def字头对齐，必须缩进

import math
def quadratic(a,b,c=0):
	if not isinstance(a,(int,float)):
		raise TypeError('兄弟，类型错了')
		return
	elif not isinstance(b,(int,float)):
		raise TypeError('兄弟，类型错了')
		return
	elif not isinstance(c,(int,float)):
		raise TypeError('兄弟，类型错了')
		return
		#好像不要return也一样,raise返回异常后就不会执行了
	else:
		delta=b**2-4*a*c
		if(delta<0):
			print('无实数解')
			return
		else:
			x1=(-b+math.sqrt(delta))/2*a
			x2=(-b-math.sqrt(delta))/2*a
	return x1,x2
#return语句用来从一个函数返回,即跳出函数
#函数第一次导入才有效，第二次导入不会覆盖；关掉python再次导入才能重新导入；
#或者用reload()