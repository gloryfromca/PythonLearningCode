class person(object):
	name="zhanghui"
zhanghui=person()
print(zhanghui.name)
zhanghui.name='zz'
print(zhanghui.name)
print(person.name)
del zhanghui.name
print(zhanghui.name)
del person.name
# print(zhanghui.name)#error

