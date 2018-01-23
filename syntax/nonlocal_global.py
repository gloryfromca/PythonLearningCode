def test():
	def do_local():
		spam = "local spam"
	def do_nonlocal():
		nonlocal spam    
		spam = "nonlocal spam"
	def do_global():
		global spam
		spam = "global spam"
	spam = "test spam"
	do_local()
	print("after local assignment:", spam)   #输出：test spam
	do_nonlocal()
	print("after nonlocal asssignment:", spam)   #输出：nonlocal spam
	do_global()
	print("after global assignment:", spam)    #输出：nonlocal spam

test()
print("in global scope:", spam)  #输出：global spam
