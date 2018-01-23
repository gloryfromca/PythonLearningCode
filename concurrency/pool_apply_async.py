from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random())#等待,没有这个将会显示按照順序，可能是因为每个进程的时间都相同
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))
    # print('Task %s runs %0.2f seconds.' % (name, start))
    # print('non_block_Task %s runs %0.2f seconds.' % (name, end))
def long_time_task1(name):
    print('Run non_block_task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random())#等待,没有这个将会显示按照順序，可能是因为每个进程的时间都相同
    end = time.time()
    # print('non_block_Task %s runs %0.2f seconds.' % (name, (end - start)))
    # print('non_block_Task %s runs %0.2f seconds.' % (name, start))
    print('end_time %s runs %0.2f seconds.' % (name, end))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(7)
    for i in range(7):
        # p.apply(long_time_task, args=(i,))#执行函数的功能，现在已经被取代，没有使用的意义。
        p.apply_async(long_time_task1, args=(i,))#非阻塞，不按照顺序执行；谁用时短，谁结果先来
        print(i)
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()#注释掉就会不等进程池结束了
    print('All subprocesses done.')
