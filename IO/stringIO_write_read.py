from io import StringIO
d=StringIO('123')
print(d.tell())
print(d)
print(d.tell())
print(d.getvalue())
print(d.tell())#0
r=d.readline()
print(d.tell())#3
print (r)#r能读出来东西
print('------------------')
s=StringIO()
print(s.tell())
print(s)
s.write('456')
print(s.tell())#3
f=s.readline()#前面write,这里read不出来东西
print(s.tell())
print(s.getvalue())#一定可用
print(s.tell())
print(f)#无结果，print为空的一行
s.seek(0)#重置为0才能顺利输出
f=s.readline()
print(f)#有结果

