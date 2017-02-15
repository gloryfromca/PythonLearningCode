

import time, sys, queue
from multiprocessing.managers import BaseManager

# 创建类似的QueueManager:
class QueueManager(BaseManager):
    print('---------')#注意这里建立的queuemanager类和manager.py的不一样，也能运行
    pass

# 由于这个QueueManager只从网络上获取Queue, 所以注册时只提供名字
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')#可以视为传入参数，并运行类中的方法！！！！！！

# 连接到服务器, 也就是运行task_master.py的机器
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)
# 端口和验证码注意保持与task_master.py设置的完全一致:
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# 创建manager并将地址、authkey作为参数传进去，就像登录一样
try:
    m.connect()
except :
    print('请先启动task_master.py!')
    sys.exit("sorry, goodbye!");

# 获取Queue对象:
task = m.get_task_queue()
result = m.get_result_queue()
time.sleep(1)#等着把任务写进去
# 从task队列取任务, 并把结果写入result队列:
for i in range(10):
    try:
        n = task.get()
        print('run task %d + %d...' % (n, n))
        r = '%d + %d = %d' % (n, n, n+n)
        # time.sleep(1)
        result.put(r)
    except queue.Empty:# 老师的是Queue.Empty 我这里报错了, 改为 queue.Empty
        print('task queue is empty.')

# 处理结果:
print('worker exit...')

if __name__ == '__main__':
    pass