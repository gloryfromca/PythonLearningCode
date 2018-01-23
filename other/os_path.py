import os
print(os.name)
#print(os.unname()) #windows 不提供该函数
print(os.environ)
print(os.environ.get('PATH'))
print('-----------------------')
print(os.path.abspath('.'))
print(os.path.join(os.path.abspath('.'),'testdir'))#
print(os.path.join('//Users//Administrator//Desktop//python_code','testdir'))
print(os.path.join('\\Users\\Administrator\\Desktop\\python_code','testdir'))
# 注意windows下是\\，Linux下是/
# print(os.path.join('\Users\Administrator\Desktop\python_code','testdir'))
# error windows下不能直接用\
print(os.path.join(r'\Users\Administrator\Desktop\python_code','testdir'))
#但是可以用r'stuff'的形式，表示stuff是个字符串
print(os.path.split(os.path.join(r'\Users\Administrator\Desktop\python_code','testdir')))
#注意看显示字符串是//，而不是/，证明还没有print，只是存储的形式。
print(os.path.splitext(os.path.join(r'\Users\Administrator\Desktop\python_code','testdir')))
# 分离文件扩展名
os.mkdir(os.path.join(r'\Users\Administrator\Desktop\python_code','testdir'))
#这个才是创建目录的函数mkdir
os.rmdir(os.path.join(r'\Users\Administrator\Desktop\python_code','testdir'))
#这个是删除目录的函数rmdir
print('----------------------')
def dir_substract1():
	return os.path.split(os.path.abspath('.'))[0]

#下面是查找含有字符串的file的相对路径
def return_path(str,x):
	abspathlen=len(x)
	a=[]
	def findfile(str,x,abspathlen):
		for n in os.listdir(x):
			if os.path.isdir(n):
				findfile(str,os.path.join(x,n),abspathlen)
			else:
			 if str_in_name(str,n):
			 	a.append(os.path.join(x,n)[abspathlen+1:])#相对地址，此处认为相对于当前目录下的文件
			 	# a.append(os.path.join(x,n))#绝对地址
		return a	
	def str_in_name(str,x):
		if len(x)<len(str):
			return False
		for index,n in enumerate(x):
			if n==str[0]:
				if len(x)-index>=len(str):
					if str==x[index:index+len(str)]:#注意[ index；index+1]的用法
						return True
				else:
					return False


	for x in findfile(str,x,abspathlen):
		x.replace('\\','/')#相对路径用/作为分隔符
		#变量存储的时候就是\\,打印出来变成了\
		# x.raplace('\',r'/')#error
		print(x)

if __name__=='__main__':
	print(dir_substract1())
	print('----------------------')
	return_path('111',os.path.abspath('.'))
