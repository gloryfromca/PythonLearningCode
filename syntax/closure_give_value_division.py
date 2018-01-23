def m(n):
    funcs=[]
    for x in range(0,n):
        def func(b):
            return x*b
        funcs.append(func)
    return funcs
ms=m(10)#只有n参数没有内部定义的函数的b参数；ms是一个元素为函数的list
print(ms[2](3))#对于list的单个函数,()内的参数将会赋给b
print(ms[7](3))
#可以起到decorator的作用