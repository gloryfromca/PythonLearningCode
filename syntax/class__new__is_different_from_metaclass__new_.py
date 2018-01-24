class A(object):
    def __new__(cls, *args, **kwargs):
        print("new")
        print(args)
        print(cls)
        Ainstance = object.__new__(cls)
        print(Ainstance)
        print("exit new")
        return Ainstance
    def __init__(self, *args, **kwargs):
        print("class init")
        print(args)
        pass

A("your") 

print("=======================================")

class Metaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs["in_meta"] = "in_new"
        returnIsClass = type.__new__(cls, name, bases, attrs)
        print(returnIsClass)
        return returnIsClass
    
class A(object, metaclass = Metaclass):
    def __init__(self, *args, **kwargs):
        print("instance init")

s = A()
s1 = A()
print(s1.in_meta)
