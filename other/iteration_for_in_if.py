import os
print([d for d in os.listdir('.')])
d={'a':'a',0:'s',(2,):'e'}
for k,v in d.items():
	print(k,'=',v)
d={'a':'a','0':'s','(2,)':'e'}
for k,v in d.items():
	print(k+'='+v)
print('------------------------------------')
L1=['Hello', 'World', 18, 'Apple', None]

for s in L1:#前面多了个逗号，没通过
	if(isinstance(s,str)):
		print(s.lower())
	else :
		print(s)


print([s.lower() for s in L1 if isinstance(s,str)])

	
print(isinstance(s,str) for s in L1)
print([isinstance(s,str) for s in L1])




