import socket
import threading
import time
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',8768))
s.listen(5)
print('waiting for connect...')

def tcplink(sock,addr):
    while True:
        data=sock.recv(1024)
        print('recv')
        if data.decode('utf-8')=='exit':
            break
        if not data:
            s.send(b'why don\'t you send data in time?')
        else:
            sock.send(b"hello"+data)
    sock.close()

while True:
    sock,addr=s.accept()
    th=threading.Thread(target=tcplink,args=(sock,addr))
    th.start()







