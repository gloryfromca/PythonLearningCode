class Metaclass(type):
    def __init__(cls, name, bases, attrs):
        attrs["in_meta"] = "in_init"
        cls.in_init = "add_in_init"
        print(cls)
        print(type(name))
        print(bases)
        cls.ss()
        #cls.s()
        
        
    def __new__(cls, name, bases, attrs):
        attrs["in_meta"] = "in_new"
        print("new")
        return type.__new__(cls, name, bases, attrs)
    
class A(object, metaclass = Metaclass):
    def __init__(self, *args, **kwargs):
        print("instance init")
        pass
    @staticmethod
    def ss():
        print("in staticMethod")
    def s(self):
        print("in instanceMethod")

s = A()
s1 = A()
print(s1.in_meta)
print(s1.in_init)
