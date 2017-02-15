from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))


if __name__=='__main__':
    p = Pool(10)
    for i in range(7):
        # time.sleep(random.random()*2)
        p.apply(long_time_task, args=(i,))

    print('Waiting for all subprocesses done...')

    for i in range(7):#等待时间
        time.sleep(random.random()*2)
        print('test %s'%i)
    print('Waiting test...')

    for i in range(7):
        p.close()
        p.join()#之星发现没有循环，close()方法只能用一次
        print('test %s'%i)
    print('Waiting test...')

    for i in range(7):
        print('test %s'%i)
    print('Waiting test...')