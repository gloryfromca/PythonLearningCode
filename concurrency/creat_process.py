from multiprocessing import Process
import os
def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)
print('------+++-----------')#放在这里也会出现两次，一次父进程，一次子进程
if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    # print('------+++-----------')#放在这里会出现一次，子进程执行的话时候if条件不满足
if not __name__ == '__main__':
    print('--------------------')#放在这里也会出现一次，子进程时出现
