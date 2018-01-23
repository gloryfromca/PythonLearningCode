def count():  
    fs = []  
    for i in range(1, 4):  
        def f(j):  
            def g():  
                return j*j  
            return g  
        fs.append(f(i))  #运行结果返回的是函数
    return fs  
  
f1, f2, f3 = count()  
#print (f1, f2, f3) 
print (f1(), f2(), f3()  )# 1 4 9
print('----------------------')
def count():  
    fs = []  
    for i in range(1, 4):  
        def f():  
            def g():  
                return i*i  
            return g  
        fs.append(f) #返回的是个函数，运行的结果返回的还是个函数
    return fs  
  
f1, f2, f3 = count()  
  
print (f1(), f2(), f3() )# 三个不同内存地址的函数 
print (f1()(), f2()(), f3()() )# 9 9 9 
#print (f1, f2, f3) 
print('----------------------')
def count():  
    fs = []  
    for i in range(1, 4):  
        def f(i):  
            def g():  
                return i*i  
            return g  
        fs.append(f(i))  #运行结果返回的是函数
    return fs  
  
f1, f2, f3 = count()  
  
print (f1(), f2(), f3()  )# 1 4 9
print('----------------------')

def count():  
    fs = []  
    for i in range(1, 4):  
        def f(i):     
           return i*i       
        fs.append(f(i))  #返回一个参数为i的f函数的运行结果（后面跟着()，代表运行）
    return fs  
  
f1, f2, f3 = count() 
#print(count()) 
print (f1, f2, f3)  
#print (f1(), f2(), f3())# 1 4 9
print('----------------------')

def count():  
    fs = []  
    for i in range(1, 4):  
        def f():     
           return i*i        
        fs.append(f)  #返回一个函数，并不是函数的运行结果（而函数的内容的是lambda i:i*i）
    return fs  
  
f1, f2, f3 = count()  
#print (f1, f2, f3)  
print (f1(), f2(), f3())# 9 9 9
print('----------------------')

def count():  
    fs = []  
    for i in range(1, 4):  
        def f():     
           return i*i        
        fs.append(f())  #返回一个函数的运行结果
    return fs  
  
f1, f2, f3 = count()  
print (f1, f2, f3)  
#print (f1(), f2(), f3())# 1 4 9

