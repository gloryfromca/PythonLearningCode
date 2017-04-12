import socket
import time
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',8768))
# data=s.recv(1024)#如果没有send（）过来的数据的话，进程会卡在这个函数这里。
for data in [b'1',b'2',b'3']:
	if data ==b'2':
		time.sleep(10)
	s.send(data)
	s.send(data)
	s.send(data)
	s.send(data)
	s.send(data)
	s.send(data)
	s.send(data)
	#如果有多个send（）同时过去的话，可能服务器进程recv（）会收到其中几个：取决于服务器进程两个recv()之间的时间，时间长的话，send（）过去的数据堆积起来。
	#send()中没有数据，不等于没有send（），只有服务器进程的recv（）接收后才知道有没有数据.
	print("'"+data.decode('utf-8')+'\'已经发送！')
	print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()

