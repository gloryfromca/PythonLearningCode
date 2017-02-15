# with open(r'C:\Users\Administrator\Desktop\python_code\test.py','r') as f:# Ture 读取本文件了！！！！！
#with open('C:/Users/Administrator/Desktop/python_code/test.py','r') as f:# Ture
with open('/Users/Administrator/Desktop/python_code/test.txt','r') as f:# Ture
# with open('/Administrator/Desktop/python_code/test.py','r') as f: #error
	# print(f.read())#一下读完出来，后面的读不出来东西了
	#print(f.read(16))#一个汉字，一个字母都算一个，还有换行符
	
	print(f.readline().strip())
	print(f.readline().strip())
	print(f.readline().strip())
	# print(f.readlines())
	# for line in f.readlines():
	#  	print(line)
	
	# for line in f.readlines():
	#  	print(line.strip())
	a=[]
	for line in f.readlines():
	 	a.append(line.strip())#strip去除行尾的\n
	 	print(a)
