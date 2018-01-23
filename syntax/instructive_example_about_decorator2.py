
def log(test):
    print('我只会出现一次')
    if isinstance(test,str):  
        def wrapper(func):
            print('wrapper执行了，我出现了几次？')
            def wrapper1():
                print('wrapper1执行了，我应该一直会出现')
                print('变身成功！')
                return 1
            return wrapper1
    else:
        def wrapper():
            print('我很简单，return都没有')


    return wrapper

@log('balabala变身')
def f():
    pass
f()
print(f())
print('------------------------------')
@log
def f():
    pass
f()
print(f())


