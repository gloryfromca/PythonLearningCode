a= [1,2,3,4]
new_a=[]
for i in a:
	if i == 1:
		new_a.append('1')
	elif i == 2:
		new_a.append('22')
	else:
		new_a.append(i)
a = new_a
print(a)




#基本目的是将a遍历，根据元素的不同返回一个值，这个值在最后结果的list中的索引和这个元素的索引相同
#也就是进去一个多长的list，出来一个多长的list；同样索引位置的元素是输出和输入的关系
#可以改写成map
#记得加list（）将map变成 list


a = list(map(lambda i : '1' if i == 1 else ( '22' if i == 2 else i ),[1,2,3,4]))
print(a)