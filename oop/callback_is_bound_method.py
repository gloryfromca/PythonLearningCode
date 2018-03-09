class A():
    def ss(self, value):
        print(self)
        print(value)
a = A()

class B():
    def __init__(self):
        self._callback = None
    def set_callback(self, func):
        print(func)
        self._callback = func
    def callback_A(self, value):
        #_callback is not B's method, So won't call it with self passed, but call it by calling it's __call__() method.
        self._callback(value)
    def justPrint(self, AString):
        print("self is", self)
        print("AString: ", AString)
    def useOtherMethod(self, AString):
        self.justPrint(AString)
b = B()
b.set_callback(a.ss)
b.callback_A("value")
b.useOtherMethod("aaa")
