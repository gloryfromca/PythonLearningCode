
class Metaclass1(type):
    def __init__(cls, name, bases, attrs):
        attrs["in_meta"] = "in_init"
        cls.in_init = "add_in_init"
        print("aaa")
        
    def __new__(cls, name, bases, attrs):
        attrs["in_meta"] = "in_new"
        print("new")
        return type.__new__(cls, name, bases, attrs)
    
class A(object, metaclass = Metaclass1):
    def __init__(self, *args, **kwargs):
        print("instance init")
        pass

s = A()
s1 = A()
print(s1.in_meta)
print(s1.in_init)

print("=======================================")

class Metaclass2(type):
        
    def __new__(cls, name, bases, attrs):
        attrs["in_meta"] = "in_new"
        print("new")
        return type.__new__(cls, name, bases, attrs)
    
class A(object, metaclass = Metaclass2):
    def __init__(self, *args, **kwargs):
        print("instance init")
        pass

s = A()
s1 = A()
print(s1.in_meta)
#print(s1.in_init)

print("=======================================")

class Metaclass3(type):
    def __init__(cls, name, bases, attrs):
        attrs["in_meta"] = "in_init"
        cls.in_init = "add_in_init"
        print("aaa")
    
class A(object, metaclass = Metaclass3):
    def __init__(self, *args, **kwargs):
        print("instance init")
        pass

s = A()
s1 = A() 
#print(s1.in_meta)
print(s1.in_init)

print("=======================================")

class Metaclass4(type):
    def __init__(cls, name, bases, attrs):
        attrs["in_meta"] = "in_init"
        cls.in_init = "add_in_init"
        print("aaa")
        return type.__new__(cls, name, bases, attrs)
        
    def __new__(cls, name, bases, attrs):
        attrs["in_meta"] = "in_new"
        print("new")
        
class A(object, metaclass = Metaclass4):
    def __init__(self, *args, **kwargs):
        print("instance init")
        pass
# you must return class in __new__
# s = A()

print("=======================================")

class SingleMeta(type):
    def __init__(cls, name, bases, attrs):
        cls._instance = None
        #cls.__new__ is object.__new__
        #it can't add parameters in it. 
        __new__o = cls.__new__
        
        print('single meta init')
        @staticmethod 
        def __new__(cls, *names, **kwargs):
            print('single meta new')
            print(names)
            print(kwargs)
            if cls._instance:
                return cls._instance
            print("ass")
            cls._instance = cv = __new__o(cls, *names, **kwargs)
            return cv
        cls.__new__ = __new__
class A(object, metaclass = SingleMeta):
    def __init__(self, *args, **kwargs):
        pass

a1 = A()
#object() takes no parameters ,so if you comment out code line above
# it will raise error
a2 = A("2", "5")

