def aa(n=1):
	if n >100:
		return 'aa'
	else:
		return aa(n+1)
s=aa()
print(s)

def aa(n=1):
	if n >100:
		return 'aa'
	else:
		aa(n+1)
s=aa()
print(s)