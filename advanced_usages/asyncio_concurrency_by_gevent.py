import time
from datetime import date#输出日期
from datetime import timedelta
import datetime

from gevent import monkey
import gevent
from gevent import socket
import hashlib
import json
monkey.patch_all()


def retry_control(max_retry_n, retry_wait_arg, func_info):    
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
                    time.sleep(wait_sec)
                i += 1
        return inner
    return decorator

#准备数据
test_user_data = ['A100','A111', 'A212','A123','A223','A623','A1323','A2413','A993', 'A941']
result_dict = {}

@retry_control(3, 1, 'socket')
def get_io_return():

    global test_user_data
    global result_dict
    
    while True:
        #
        print('begin sleep!')
        time.sleep(8)
        print('wake!')

        try:
            customer_id = test_user_data[0]
            test_user_data.pop(0)   

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

            #每次建立socket
            socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1) 
            socket_.connect(("334.68.88.15", 95))#内网生产
            
            #获得报文信息
            socket_.sendall(will_send)
            get_info_ =  socket_.recv(1024)



            get_info = get_info_.decode('gbk')[40:]
            print(get_info)
            #关闭socket
            socket_.close()
            
            #准备输出
            get_info_json = json.loads(get_info)
            customer_pid = get_info_json['message']['CUSTOMERPID']
            customer_phone = get_info_json['message']['DEUSERID']
            result_dict[customer_id] = customer_phone
            

        except IndexError as e:
            return 'IndexError Done' 





gevent.joinall([
    gevent.spawn(get_io_return),
    gevent.spawn(get_io_return),
    gevent.spawn(get_io_return),
    gevent.spawn(get_io_return),
    gevent.spawn(get_io_return),
    ])

print('==== result ====')
print(test_user_data)
print(result_dict)
print('==== result ====')


