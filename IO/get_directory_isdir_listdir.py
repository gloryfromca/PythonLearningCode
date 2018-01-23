import os
def print_drectory(spath,n=0):
	if n==0:
		print(spath)
	for item in os.listdir(spath):
		item=os.path.join(spath,item)
		if os.path.isdir(item):
			print(" "*n,"|",item)
			print_drectory(os.path.join(spath,item),n+2)
		else:
			print(" "*n,"|",item)

print_drectory("D:\\")