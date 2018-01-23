import base64


a='zhanghui张辉'
a=a.encode('utf-8')
print(a)
print(type(a))
# b=a.decode('utf-8')
# print(b)
# print(type(b))
a=base64.b64encode(a)
print(a)
print(type(a))
a=a.decode('utf-8')
print(a)
print(type(a))
a=base64.b64decode(a)
print(a)
print(type(a))

print('####################')
a=b'zhanghui'
a=base64.b64encode(a)
print(a)#bytes
print(type(a))
a=a.decode('ascii')
# a=a.decode('utf-8')
print(a)
print(type(a))
a=base64.b64decode(a)
print(a)
print(type(a))
print('####################')


a='11111sfddhzu'
print(a)
print(type(a))
a=b'11111sfddhzu+-'#ascii码表示的二进制数据，并不能直接用来b64decode
# a=base64.b64decode(str(a)[2:-1])#，对base64解码的string补齐等号就可以了
print(a)#转换为二进制用的是ASCII码
print(type(a))
a=b'zhanghui'
print('aaaaaaaaa')
a=base64.b64encode(a)
print(a)#bytes
print(type(a))
print(str(a)[2:-1])
#str如何转化为二进制
print('aaaaaaaaaaaaa')
print(str(a))
a=base64.b64decode(str(a)[2:-1])
print(a)
print(type(a))

print('00000000')
a=base64.b64encode(a)
print(a)
print(type(a))

# a=b'11111sfddhzuz账户'
#含有中文就报错，因为转换为二进制用的是ASCII码
print('----------------')
a='11111sfddhzu'.encode()#可能默认utf-8
print(a)
print(type(a))
a='11111sfddhzu张辉'.encode()#可能默认utf-8
print(a)
print('##############')
a='11111sfddhzu张辉'.encode('utf-8')
print(a)
print(str(a))
print(str(a)[0])

print(type(a))
a=base64.b64encode(a)
print(a)
print(type(a))

print('----------')

from email.header import Header
b=Header('asafdus张辉','utf-8').encode()
print(b)
print(type(b))
c=Header('asafdus张辉').encode()#这里的encode应该是重写过的
print(b)
print(type(b))

