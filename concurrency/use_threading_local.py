import threading
local_school=threading.local()
def adding_sutdent(name):
	local_school.student=name
	reading_student()
def reading_student():
	std=local_school.student
	print(std)
t1=threading.Thread(target=adding_sutdent,args=('Alice',))
t2=threading.Thread(target=adding_sutdent,args=('Bob',))
t1.start()
t2.start()
t1.join()
t2.join()

