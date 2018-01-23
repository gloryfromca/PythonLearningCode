def person(name, age, *args, city, job):#正常
    print(name, age, city, job)
person(1,2,3,4,5,city=12,job=12133)

def person(name, age, *, city, job):#不接受可变参数，给多了位置参数报错
    print(name, age, city, job)
person(1,2,3,4,5,city=12,job=12133)

def person(name, age, *args, city, job,**kargs):#即使一个是位置参数，一个是关键字参数，依然因为参数重名报错
    print(name, age, city, job)
person(1,2,3,4,5,city=12,job=12133,age='age')

def person(name,dd,uu,address ='sh',ss = 1 ,age=None,*,age):#出错，验证：即使一个是位置参数，一个是关键字参数，依然因为参数重名报错
    print(name, age)
person(1,2,3,age=123)

def person(name,dd,uu,address ='sh',ss = 1,age=None,**kargs):#出错，上面的重名限制的为了预防此种情况
    print(name, age)
person(1,2,3,4,5,6,age=123)

def person(name, age, *args, city, job,**kargs):#正常
    print(name, age, city, job)
person(1,5,3,4,5,city=12,job=12133)

def person(name, age=None,*):#格式出错，*号之后需要加一个变量名字接受参数，此处的出现形式毫无意义
    print(name, age)
person(1,age=123)

def person(name,dd,uu,address ='sh',ss = 1,age=None,*,**kargs):#格式出错，此种情况*的出现也毫无意义
    print(name, age)
person(1,2,3,age=123)

def person(name,dd,uu,address ='sh',ss = 1,age=None,**kargs):#正常
    print(name, age)
person(1,2,3,age=123)

def person(name, age=None,*args):#正常
    print(name, age)
person(1,age=123)

def person(name, ss = 1 ,age=None,**kargs):#正常，默认参数传入颠倒顺序也没有问题
    print(name,ss, age)
person(1,age=123,ss=1)

def person(name, ss = 1 ,age=None,**kargs):#正常，应该被传入到kargs关键字参数被放在了传入的默认参数前面也没问题
    print(name,ss, age,kargs)
person(1,age=123,dd=1,ss=1)

def person(name, ss = 1 ,age=None,*,dd,**kargs):
    print(name,ss, age,kargs)
person(1,age=123,dd=1,ss=1)

def person(name, age=None):#正常
    print(name, age)
person(1,age=123)

def person(name, ss = 1 ,age=None):#正常，用关键字参数的形式传入默认参数，用来跳过某些默认参数；但不能跳过位置参数
    print(name, age)
person(1,age=123)

def person(name,aa, address ='sh',ss = 1 ,age=None):#出错，传入参数时候,先把位置参数形式的参数按照顺序传给位置参数和默认参数，导致覆盖了address参数
    print(name, age)
person(1,1,2,4,address=1)

def person(name,aa, address ='sh',ss = 1 ,age=None,**a):#正常
    print(name, age)
person(1,1,4,dodo=1,ss=1)



def person(name,address ='sh',aa, ss = 1 ,age=None):#出错，传入参数时候，必须让age=123的形式位于位置参数的后面
    print(name, age)
person(1,age=123,1,2)
#所有的age=123形式的参数都必须是在直接传参数的形式的后面
