import base64
b='zhanghui张辉'
b=b.encode('utf-8')
print(b)
e=base64.b64encode(b)
print(e)
if e==b'emhhbmdodWnlvKDovok=':
    print('yes')
f=e.decode('utf-8')
print(f)
s=e.decode('ascii')
print(s)
g=base64.b64decode(s)
print(g)
print('----------------')
b='zhanghui张辉'
b=b.encode('utf-8')
e=base64.b64encode(b)
print(b)#转换为utf-8代码
print(e)
a=str(e)
print(a)
c=a[2:-1].encode('ascii')#将字符串形式的base编码变为二进制
if c==e:
  print('yes')
print(c)
d=base64.b64decode(c)
print(d)
d=base64.b64decode(a[2:-1])
print(d)
