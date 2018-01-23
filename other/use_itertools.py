import itertools
natuals=itertools.count(1)
s=itertools.repeat('a',3)
for n in s:
	print(n)
ns=itertools.takewhile(lambda x:x<=10,natuals)
print(ns)
print(type(ns))
print(list(ns))
for c in itertools.chain('ABC', 'XYZ'):
	print(c)
for key,group in itertools.groupby('aAAaHhHUu'):
	# print(key,group)
	print(key,list(group))
for key,group in itertools.groupby('aAAaHhHUu',lambda c:c.upper()):
	print(key,list(group))
	
