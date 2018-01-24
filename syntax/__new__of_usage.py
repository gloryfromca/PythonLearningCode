class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        print('in new')
        if cls._instance:
            return cls._instance
        cls._isntance = cv = object.__new__(cls, *args, **kwargs)
        return cv
    def __init__(self):
        print("in init")


sin1 = Singleton()
sin2 = Singleton()
print(sin1 is sin2)
print(sin1 )
print( sin2) 

print('===============')
class SingleMeta(type):
    def __init__(cls, name, bases, attrs):
        cls._instance = None
        __new__o = cls.__new__
	print(__new__o) #A的new方法，实际上是继承的object方法
        print('single meta init')
        @staticmethod #Python3中有没有好像没什么区别，__new__是一个静态方法
        def __new__(cls, *args, **kwargs):
            print('single meta new')
            if cls._instance:
                return cls._instance
            cls._instance = cv = __new__o(cls, *args, **kwargs)
            return cv
        cls.__new__ = __new__
class A(object , metaclass = SingleMeta):
    pass
#元类也可以有初始化__init__函数，能够更好地改变类创建时候的行为。
#除此之外，class中的__new__的参数就是__init__的参数，而元类的参数则有四个，提供了更多灵活性。
a1 = A()  
a2 = A()  #传给类的元类自身的__init__只有一次，实际类的初始化会调用元类的实例中的__new__方法

print('===============')


class TraceAttribute(type):
    def __init__(cls, name, bases, dict):
        __getattribute__o = cls.__getattribute__

        def __getattribute__(self, *args, **kwargs):
            print('__getattribute__:', args, kwargs)
            return __getattribute__o(self, *args, **kwargs)
        cls.__getattribute__ = __getattribute__ #元类也可以重写类的某些函数，能够更好地改变类创建时候的行为

class A(object, metaclass=TraceAttribute): 
    __metaclass__ = TraceAttribute
    a = 1
    b = 2
a = A()
a.a
# output: __getattribute__:('a',){}
a.b
