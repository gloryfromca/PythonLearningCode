class a(object):
	def __init__(self):
		print('first:init')
	def __call__(self):
		print('second:call')
instance=a()
print(instance)
instance_method=a()()
print(instance_method)




