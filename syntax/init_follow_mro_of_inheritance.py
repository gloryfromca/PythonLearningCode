class A(object):
    def __init__(self):
        print('use A init')
class B(object):
    def __init__(self):
        print('use B init')
class C(A,B):
    def __init__(self):
        super(C,self).__init__()
c = C()
print(c)

print('=========================')
class Init(object):
    def __init__(self, value):
        print('Init')
        self.val = value
class Add2(Init):
    def __init__(self, val):
        print('Add2')
        super(Add2, self).__init__(val)
        self.val += 2
class Mul5(Init):
    def __init__(self, val):
        print('Mul5')
        super(Mul5, self).__init__(val)
        self.val *= 5
class Pro(Mul5, Add2):
    pass
class Incr(Pro):
    csup = super(Pro)
    def __init__(self, val):
        print("Incr")
        self.csup.__init__(val)
        self.val += 1
p = Incr(5)
print(Incr.__mro__)
print(p.val)       
#实际的初始化按照mro顺序进行一遍；print结果不反映顺序 

print('=========================')
class Init(object):
    def __init__(self, value):
        print('Init')
        self.val = value
class Add2(Init):
    def __init__(self, val):
        print('Add2')
        super(Add2, self).__init__(val)
        self.val += 2
class Mul5(Init):
    # def __init__(self, val):
    #     print('Mul5')
    #     super(Mul5, self).__init__(val)
    #     self.val *= 5
    pass
class Pro(Mul5, Add2):
    pass
class Incr(Pro):
    csup = super(Pro)
    def __init__(self, val):
        print("Incr")
        self.csup.__init__(val)
        self.val += 1
p = Incr(5)
print(Incr.__mro__)
print(p.val)       
#实际的初始化按照mro顺序进行一遍；print结果不反映顺序 
        