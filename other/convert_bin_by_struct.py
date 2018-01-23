import struct
a=struct.pack('>I',10240099)
print(bin(1024009910240099))
print(a)
print(len(a))#4，四个字节长
a1=struct.unpack('>I',a)
print(a1)
a2=struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')#bytes以字节为基本元素的对象
print(a2)
print(type(b'\xf0\xf0\xf0\xf0\x80\x80'))

a='徐'
print(ord(a))
b=bytes(a,'utf-8')
print(b)
print(b.decode())

# with open('/C:/Users/Administrator/Desktop/popon1.bmp','rb') as f:#error about /C:
with open('\\Users\\Administrator\\Desktop\\popon1.bmp','rb') as f:
# with open('/Users/Administrator/Desktop/popon1.bmp','rb') as f:#true
	a=f.read(30)
print(a)
b=struct.unpack('<ccIIIIIIHH',a)#c代表字节
print(b)
def bmpinfo(path):
	try:	
		with open(path,'rb') as f:
			a=f.read(30)
	except FileNotFoundError as e:
		# raise
		print(e) 	
	if struct.unpack('<ccIIIIIIHH',a)[0:2]==(b'B',b'M'):
		return (struct.unpack('<ccIIIIIIHH',a)[2],struct.unpack('<ccIIIIIIHH',a)[9])
	else:
		return False
print(bmpinfo('\\Users\\Administrator\\Desktop\\popon1.bmp'))
# print(bmpinfo('Users\\Administrator\\Desktop\\popon1.bmp'))#error

print(type(ValueError))