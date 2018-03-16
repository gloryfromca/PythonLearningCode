print("使用装饰器实现单例模式：啰嗦版")
class Singleton(object):  

    def __init__( self, decorated ):  
        self._decorated = decorated  
        print(self._decorated)#<class '__main__.MyClass'>
        print("init")

    def Instance( self ):  
        try: 
            print(self)#<__main__.Singleton object at 0x0000000000A5B5F8>
            print(self._instance)#<class '__main__.MyClass'>
            print("aaa")
            return self._instance  
        except AttributeError:  
            self._instance = self._decorated()  
            return self._instance  
        
    #you don't need to write method below. 
    #def __call__( self ):  #阻止MyClass实例化,因为Singleton(MyClass)()被阻止了。
        #raise TypeError( 'single instance allowed' ) 

    def MyClass_is_turned_to_Singleton_instance(self):
        print("MyClass_is_turned_to_Singleton_instance")


@Singleton  #encountering Syntactic sugar will imediately execute.So will it print "init"
#把MyClass类作为参数传进@Singleton装饰器，返回一个Singleton类的实例。之后初始化Singleton，其中decorated参数就是MyClass类。
class MyClass(object):  
    def __init__( self ):  
        print( 'created' )  

#调用装饰器Singleton的过程发生了初始化,MyClass=Singleton(MyClass)
print(MyClass)
print("=========after init=============")
myClass1=MyClass.Instance()
print("=========myclass 2=============")
myClass2=MyClass.Instance()
print(myClass1)
print(myClass2 is myClass1)
MyClass.MyClass_is_turned_to_Singleton_instance()
# raise TypeError( 'single instance allowed' )  
# myClass3=MyClass() 

print("使用装饰器实现单例模式：正常版，不能重复初始化")
class Singleton(object):  

    def __init__( self, decorated ):  
        self._decorated = decorated  

    def __call__( self ):  
        try: 
            return self._instance  
        except AttributeError:  
            self._instance = self._decorated()  
            return self._instance  

@Singleton
class MyClass(object):  
    def __init__( self ):  
        print( 'created' )  

myClass1=MyClass()
myClass2=MyClass()
print(myClass1)
print(myClass2)


print("使用元类实现单例模式：特殊单例，同一对象可重复初始化")
print("更改类实例初始化时候调用的的__new__，它是一个闭包，会保存单例")
print("能够重复初始化的原因是用class的__new__方法完成创建之后，总会走初始化")
class SingleMeta(type):
    def __init__(cls, name, bases, attrs):
        cls._instance = None
        #cls.__new__ is object.__new__
        #it can't add parameters in it. 
        __new__o = cls.__new__
        
        print('single meta init')
        @staticmethod 
        def __new__(cls, *args, **kwargs):
            print('single meta new')
            print(names)
            print(kwargs)
            if cls._instance:
                return cls._instance
            print("ass")
            cls._instance = cv = __new__o(cls)
            cls._instance.changed = "first_change" 
            return cv
        #this __new__ is cls __new__, not metaclass' __new__ 
        cls.__new__ = __new__
class A(object, metaclass = SingleMeta):
    def __init__(self, *args, **kwargs):
        print("in A init")
        print(args)
        self.changed = "second_change"
        print(kwargs)
        pass

a1 = A()
print(a1.changed)
# a2's initial parameters will be discarded.
a2 = A("2", "5")
print(a1 == a2)
print(a2.changed)




