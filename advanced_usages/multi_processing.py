

import time
from datetime import date#输出日期
from datetime import timedelta
import datetime

#当月、当天日期
current_month, now_date, now_time = datetime.datetime.now().strftime('%Y%m,%Y%m%d,%H%M%S').split(',')





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


@retry_control(3, 1, 'socket')
def worker_def(customer_id):
    import socket
    import hashlib
    import json
    import datetime
    #每次建立socket
    socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1) 
    socket_.connect(("111.118.81.15", 9115))#内网生产
    
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

                    
    #signKey = "bugaosuni"
    signKey = "bugaosuni"#生产

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
    


import time
from multiprocessing import Process, Lock, Manager
from multiprocessing import JoinableQueue
import multiprocessing
from queue import Empty
from ctypes import Structure, c_double, c_char_p, c_char


que1 = JoinableQueue()

class get_pid_phone():
    def __init__(self, x):
        self.customer_id  = x
        self.result_tag = 0
    def write_(self, result):
        self.result = result
        self.result_tag = 1
        
def get_pid_phone_by_customer_id(x, que1):
    t = get_pid_phone(x)
    que1.put(t)
    return t

test_user_data = pd.DataFrame({'customer_id':['A100','A111', 'A212','A123']*25})
test_user_data['personal_info'] = test_user_data['customer_id'][0:10].apply(lambda x:get_pid_phone_by_customer_id(x, que1))

#证明不可以进程间通过queue共享资源1
print('第一个get_pid_phone class:')
get_pid_phone_instance = test_user_data['personal_info'][1]
print(get_pid_phone_instance)
try:
    print(get_pid_phone_instance.result)
except AttributeError as e:
    print('开始并没有result属性！')

#证明进程可以继承父进程的资源1
ssd=103

s_class_counter = 1
class all():
    def __init__(self,name):
        self.name=name
    def change(self,name):
        self.name=name
    def add(self,ss):
        self.ss = ss
s_class = all('zhanghui')

#加锁
lock = Lock()

#share memory
share_num = multiprocessing.Value(c_double, 1.0, lock=lock)
share_str = multiprocessing.Array('c',100,lock=lock)
share_str.value = b'zz'

#共享manager
manager_dict = Manager().dict()
manager_dict[0] = 0


def worker1(que1,share_num, share_str, manager_dict): 
    #print('in worker1')
    #print(que1.qsize())
    #while not que1.empty():

    global s_class_counter
    global s_class
    
    while True: 
        try:
            term = que1.get(block=False)
            #获得剩余的queue长度
            print('==que1.qsize==', que1.qsize(), '==que1.qsize==')

            term_result = worker_def(term.customer_id)
            term.write_(term_result)
            setattr(term, 'writed', 'in process')   

            #获得访问接口的结果
            print('==result==', term.result, '==result==')        
            print('==term==', term, '==term==') 

            #通过共享内存的方式实现共享
            share_num.value =share_num.value+ 1
            print('==share_num==', share_num.value, '==share_num==')
            share_str.value = b'pysss'
            print('==share_str==', share_str.value, '==share_str==')
            #通过manager的方式共享
            manager_dict[term.customer_id] = term_result

	    #证明进程可以继承父进程的资源1
            print('===ssd===',ssd,'===ssd===')
	    #证明进程可以继承父进程的资源，但是一旦修改就报错。证明不可以进程间共享资源2
            #ssd+=1
            #print('===ssd===',ssd,'===ssd===')
            
            #修改继承的对象属性是可以的，但是并不会共享到父进程中
            s_class_counter+=1	
            s_class.change(s_class_counter)
            print('==s_class_name==', s_class.name, '==s_class_name==')
            #add属性也可以的，但是并不会共享到父进程中
            s_class.add('ass')
            print('==s_class_ss==', s_class.ss, '==s_class_ss==')

        except Empty as e:
            return None


print('now_time:', now_time)
p_list = []
for i in range(2) :
    p = multiprocessing.Process(target=worker1, args=(que1,share_num, share_str, manager_dict))
    p_list.append(p)
for i in p_list:
    i.start()
for i in p_list:
    i.join()
current_month, now_date, now_time = datetime.datetime.now().strftime('%Y%m,%Y%m%d,%H%M%S').split(',')
print('over_time:', now_time)

#查看父进程引用计数和类实例的属性被添加或者修改
print('s_class_counter:', s_class_counter)
print('s_class_name:',s_class.name)
try:
    print('add_attribute:', s_class.ss)
except AttributeError as e:
    print('最后并没有ss属性！')

#查看ctypes共享内存的结果
print('==share_str.value==', share_str.value, '==share_str.value==')

#查看manager共享内存的结果
print('==manager_dict==', manager_dict, '==manager_dict==')

#证明不可以进程间通过queue共享资源1
print('第一个get_pid_phone class:')
get_pid_phone_instance = test_user_data['personal_info'][1]
print(get_pid_phone_instance)
try:
    print(get_pid_phone_instance.result)
except AttributeError as e:
    print('最后并没有result属性！')
try:
    print(get_pid_phone_instance.writed)
except AttributeError as e:
    print('最后并没有writed属性！')
