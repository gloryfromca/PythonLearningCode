import socket
import hashlib
import json

import threading
import time
from queue import Queue
from queue import Empty

#实现出错重试
def retry_control(max_retry_n, retry_wait_arg, func_info):
    from time import sleep

    def decorator(func):
        def inner(*args, **kargs):
            i = 0
            while True:
                try:
                    return func(*args, **kargs),'成功'
                except Exception as e:
                    wait_sec = retry_wait_arg 
                    if i >= max_retry_n:
                        return ('',''),'已经达到最大重试次数: {}次! '.format(max_retry_n)
                    sleep(wait_sec)
                i += 1
        return inner
    return decorator

#建立socket访问接口获得数据
@retry_control(3, 1, 'socket')
def worker_def(customer_id):
    
    #每次建立socket
    socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1) 
    socket_.connect(("177.68.81.15", 9593))#内网生产
    
    #时间模块的计算
    now_date, now_time = datetime.datetime.now().strftime('%Y%m%d,%H%M%S').split(',')
    timestamp_end8 = str(datetime.datetime.now().timestamp()*10**6)[-10:-2]
    
    str_1 = "{\n" \
            + "\"transactionType\":\"CustomerIdToUser.Req\",\n" \
            + "\"branchId\":\"JR001\",\n" \
            + "\"code\":\"UTF-8\",\n" \
            + "\"orgTxDate\":\"%s\",\n"%(now_date) \
            + "\"orgTxTime\":\"%s\",\n"%(now_time) \
            + "\"orgTxLogNo\":\"%s\",\n"%(timestamp_end8) \
            + "\"requestMessage\":\n"\
            + "{\n" \
            + "\"customerId\":\"%s\"\n"%(customer_id)\
            + "}\n" \
            + "}"


    signKey = "bugaosuni"#生产signkey

    #获得MD5
    str_f = str_1 + signKey 
    md5 = hashlib.md5()
    md5.update(str_f.encode('utf8'))
    sign = md5.hexdigest()

    #获得sign拼接报文的长度，并取bytes
    sd = sign+str_1
    str_len_add8 = len(bytes(sd,encoding='utf8'))+8
    str_len_add8_bytes = str_len_add8.to_bytes(4, byteorder='big')
    str_bytes = bytes(sd,encoding='utf8')
    will_send = str_len_add8_bytes+str_bytes
    
    #获得报文信息
    socket_.sendall(will_send)
    get_info = socket_.recv(1024).decode('gbk')[40:]
    
    #关闭socket
    socket_.close()
    
    #准备输出
    get_info_json = json.loads(get_info)
    customer_pid = get_info_json['message']['CUSTOMERPID']
    customer_phone = get_info_json['message']['DEUSERID']
    
    return customer_pid , customer_phone



que1 = Queue()

class get_pid_phone():
    def __init__(self, x):
        self.customer_id  = x
        self.result_tag = 0
    def write_(self, result):
        self.result = result
        self.result_tag = 1
        
#下面的函数实现创建一个对象。1、把对象添加到queue中 2、把对象直接返回。实际就是生产者函数
def get_pid_phone_by_customer_id(x):
    t = get_pid_phone(x)
    que1.put(t)
    return t

#调用上面的生产者函数，直接返回一个对象
test_user_data['personal_info'] = test_user_data['customer_id'].apply(lambda x:get_pid_phone_by_customer_id(x))

#建立多线程准备多线程执行消费者函数
class consumer(threading.Thread):
    def __init__(self, que1):
        threading.Thread.__init__(self)
        self.que1 = que1
    def run(self):
        while self.que1.not_empty:#用这个，可能执行到后面的get的时候空掉了，然后被阻塞。所以后面的queue.get()要加block=False
            try:
                term = self.que1.get(block=False)
                term_result = worker_def(term.customer_id)
                term.write_(term_result)
#                 print('=======')
#                 print(term_result)
#                 print(que1.qsize()) 
#                 print(threading.current_thread().name)
#                 print('=======')
                self.que1.task_done()#必须有，用来说明当前取出的任务已经完成，队列长度会减少1
            except Empty as e:
                time.sleep(0.5) #等0.5秒防止慢速生产造成提前退出
                if self.que1.empty:
                    return 'all_done!'#等待0.5秒后queue仍然没有新的term直接退出

#建立多线程，并将多线程放进list中
ss= [consumer(que1) for i in range(20)]

#逐个开启多线程
for i in ss :
    i.start()

#逐个设置多线程对于主线程的阻塞，也就是主线程必须等到每一个调用了join方法的线程执行完成才能执行下去
#主线程指的就是当前执行的这个脚本
for i in ss :
    i.join()
