#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'abc'.encode('ascii')
'abc'.encode('utf-8')
'中文'.encode('utf-8')
b'abc'.decode('ascii')
b'\xe4\xb8\xad\x96\x88'.decode('utf-8')

len(b'abc')

print("b'abc'")
print(b'abc')
a=ord('中')
b=ord('文')
c=chr(a)
d=chr(b)
print(c,d)
print('\a,\b')
print('\u4e2d,\u6587')
#字符编码及相关函数、表示