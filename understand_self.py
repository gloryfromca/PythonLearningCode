class Foo(object):
    def create_new(self):
        return self.__class__()

    def create_new2(self):
        return Foo()

class Bar(Foo):
    pass

b = Bar()
c = b.create_new()
print (type(c))  # We got an instance of Bar
d = b.create_new2()
print (type(d))  # we got an instance of Foo