import time,threading
def loop():
		print('thread %s is running...'%threading.current_thread().name)
		n=0
		while n<5:
			print('thread %s >>> %s'%(threading.current_thread().name,n))
			time.sleep(0.2)
			n+=1
		print('subthread end')
print('thread %s is running...'%threading.current_thread().name)
t=threading.Thread(target=loop)
t.start()
t.join()
print('thread %s ended'%threading.current_thread().name)

