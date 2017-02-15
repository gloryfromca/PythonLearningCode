import functools
def daoluan():
    print('就一句')
    #return 1 #尝试一下注释掉的效果

print(1111)

def log(canshu):
    print("prove immediate execute")# 程序读到@会立即执行而不是加载到内存
    def wrapper():
        print('begin call')
        result =func()
        print('end call')
        return result 
    return daoluan
@log
def f():
    print('有个存在感')
f()
print(f())
print(f())
f()
print(f.__name__)
print('----------------------------------------')
def log(func):
    #@functools.wraps(func)#和它并列的只能是一个函数，而不是语句
    print("prove immediate execute")# 程序读到@会立即执行而不是加载到内存
    def wrapper():
        print('begin call')
        result =func()
        print('end call')
        return result 
    return wrapper
@log
def f():
    print('有个存在感')
f()
f()
print(f.__name__)
print('----------------------------------------')
def log(func):
    #@functools.wraps(func)#和它并列的只能是一个函数，而不是语句
    print("prove immediate execute")# 程序读到@会立即执行而不是加载到内存
    def wrapper():
        #@functools.wraps(func)#在以func参数为输入的函数内部写，表示将func的_name__赋给返回的函数。
        def wrapper2():
            print('begin call')
            result =func()
            print('end call')
            return result 
        return wrapper2()
    return wrapper

@log
def f():
    print('再次有个存在感')
f()
f()
f()
#f()
print(f.__name__)
print('----------------------------------------')
def log2(number):
    #@functools.wraps(func)#和它并列的只能是一个函数，而不是语句
    print("prove immediate execute")# 程序读到@会立即执行而不是加载到内存
    def wrapper(func):
        @functools.wraps(func)#在以func参数为输入的函数内部写，表示将func的_name__赋给返回的函数。
        def wrapper2():
            print('%s begin call'%number)
            result =func()
            print('end call')
            return result 
        return wrapper2
    return wrapper

@log2(99)
def f():#因为顺序执行的原因，下面的foo将上面的foo覆盖了。因此，在Python中代码的放置位置是有要求的，
#不能随意摆放，函数体要放在被调用的语句之前。
    print('3次有个存在感')
f()
#f()
print(f.__name__)
print('----------------------------------------')
def log3(number):
    #@functools.wraps(func)#和它并列的只能是一个函数，而不是语句
    print("prove immediate execute")# 程序读到@会立即执行而不是加载到内存
    def wrapper(func):
        @functools.wraps(func)#在以func参数为输入的函数内部写，表示将func的_name__赋给返回的函数。
        def wrapper2():
            print('%s begin call'%number)
            result =func()
            print('end call')
            return result 
        return wrapper2
    return wrapper

@log3(99)
def b():
    pass
b()
#f()
print(b.__name__)
print('----------------------------------------')
