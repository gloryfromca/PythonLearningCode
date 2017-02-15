def outer(func):
        print("认证成功！")
        result = func()
        print("日志添加成功")
        return func

@outer
def f1():

    print("业务部门1数据接口......")

f1()
f1()
f1()
print('------------------------------')
def outer(func):
        print("认证成功！")
        result = func()
        print("日志添加成功")
        return result#注意报错！！！！！

@outer
def f1():

    print("业务部门1数据接口......")

f1()
