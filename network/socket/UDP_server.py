import socket
import threading
import time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',8768))
print('waiting for connect...')

while True:
    data,addr=s.recvfrom(1024)
    print("%s:%s"%addr)
    s.sendto(b"hello%s"%data,addr)









