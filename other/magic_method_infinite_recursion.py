class A(object):
	def __init__(self,values):
		self.values = values

	def __len__(self):
		return len(self.values)
		# return len(self) #报错的原因是len(self)调用self的__len__，导致了无限的循环


a = A([1,2,3])
print(len(a))
