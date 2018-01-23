import socket
import threading
import time
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(type(s))#class:socket.socket
s.bind(('127.0.0.1',9997))#tuple
s.listen(5)

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

while True:
	sock,addr=s.accept()#accept()会等待并返回一个客户端的连接
	print(type(sock))#class:socket.socket
	print(type(addr))
	print(addr)
	t=threading.Thread(target=tcplink,args=(sock,addr))
	t.start()




