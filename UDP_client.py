import socket
import time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in [b'1',b'2',b'3']:
	time.sleep(5)
	s.sendto(data,('127.0.0.1',8768))
	data,addr=s.recvfrom(1024)
	print(data.decode('utf-8'))
s.sendto(b'exit',('127.0.0.1',8768))
s.close()

