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
            self._instance = self._decorated  
            return self._instance  
  
    def __call__( self ):  #阻止MyClass实例化,因为Singleton(MyClass)()被阻止了。
        raise TypeError( 'single instance allowed' ) 

    def MyClass_is_turned_to_Singleton_instance(self):
        print("MyClass_is_turned_to_Singleton_instance")


@Singleton  #encountering Syntactic sugar will imediately execute.So will it print "init"
#把MyClass类作为参数传进@Singleton装饰器，返回一个Singleton类的实例。之后初始化Singleton，其中decorated参数就是MyClass类。
class MyClass(object):  
    def __init__( self ):  
        print( 'created' )  

print(MyClass)#调用装饰器Singleton的过程发生了初始化,MyClass=Singleton(MyClass)
print("=========after init=============")
myClass1=MyClass.Instance()
print("=========myclass 2=============")
myClass2=MyClass.Instance()
print(myClass1)
print(myClass2 is myClass1)
myClass2=MyClass.MyClass_is_turned_to_Singleton_instance()
# myClass3=MyClass() # raise TypeError( 'single instance allowed' )  
