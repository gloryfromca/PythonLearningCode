import threading
balance=0
lock=threading.Lock()

def first_operation(n):
	global balance
	balance+=n
	balance-=n
def operation(n):
	for i in range(100000):#循环次数足够多，两个线程交替执行，产生错误结果
		lock.acquire()#使用lock，运行速度会变慢;一个线程执行,另一个等待锁被释放
		try:
			first_operation(n)
		finally:
			lock.release()


t1=threading.Thread(target=operation,args=(5,))
t2=threading.Thread(target=operation,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

