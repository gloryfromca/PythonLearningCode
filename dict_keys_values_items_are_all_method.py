d={3:4,4:5}
keys=d.items()
print(keys)
ss=type(keys)
print(ss)
d.pop(3)
print(d)
print(d.values())
print(type(d.values()))
for i in d.values():
	print(i)