class A(object):
    def __new__(cls, *args, **kwargs):
        print("new")
        print(args)
        return object.__new__(cls)
    def __init__(self, *args, **kwargs):
        print("class init")
        print(args)
        pass

A("your") 
A("name")
A("is")
