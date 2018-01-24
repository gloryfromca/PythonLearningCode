class test(object):
    def __new__(cls, name):  
        print("====in new()====")
        print(name)
        print(cls)
        print(super(test, cls))
	#super() is same as super(test, cls)
        print(super())
        print(super(cls))
        #super(cls, inst) will get inst.mro()[cls's location + 1].
        #class' mro is include itself in first bucket.
        #instance's mro can get by call property __class__ firstly.  
        print(cls.mro())
        print(test.mro())
        return super().__new__(cls)
    
    @staticmethod
    def staticway():
        print("====in staticmethod()====")
        
    def __init__(self, name):
        print("====in init()====")
        print(name)
s = test("zhanghui")
print("====in main()====")
print(s.__class__.mro())
print(test.mro())
print("====before class name====")
class name(test):
    pass
saizhi = "saizhi"
print("you can use instance method if you pass a instance into `super()`'s second place.")
super(name, name(saizhi)).__init__(saizhi)
print("you can use class method such as __new__ when you pass a class into `super()`'s second place,")
print("and you must pass necessary parameters into __new__'s parameters.")
super(name, name).__new__(name, saizhi)
super(name, name).staticway()
print("you can't use instance method such as __init__ when you pass a class into `super()`'s second place.")
super(name, name).__init__()




