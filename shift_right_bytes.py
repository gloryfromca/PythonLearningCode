
n = 10240099
print(bin(n))
print(len(bin(n)))
print(bin(n)[0:3])#当字符串来处理，则0b也被视为字符串的一部分
print(bin(n)[:-1])
b1 = (n & 0xff000000) >> 24 #将b1转换为二进制然后将变量右移24位
# b1 = (n & 0xff000000) #>> 24
print(b1)
print(bin(b1))
b2 = (n & 0xff0000) >> 16
# b2 = (n & 0xff0000) #>> 16
print(b2)
b3 = (n & 0xff00) >> 8
# b3 = (n & 0xff00) #>> 8
print(b3)
b4 = n & 0xff
bs = bytes([b1+b2, b3, b4])
print(bs)
bs = bytes([b1, b2, b3, b4])
print(bs)


