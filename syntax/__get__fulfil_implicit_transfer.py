class A(object):
    def  ss(self):
        pass
a = A()
bm = a.ss.__get__(a,A)
print("type:",type(bm))
print(dir(bm))
print(bm.__func__)
print(bm.__self__)
print('------------------')
bm = A.ss.__get__(a,A)#实现self的隐式传递
print("type:",type(bm))
print(dir(bm))
print(bm.__func__)
print(bm.__self__)
print('------------------')
unbm = a.ss.__get__(None,A)
print("type:",type(unbm))
print(dir(unbm))
print(unbm.__func__)
print(unbm.__self__)
print('------------------')
unbm = A.ss.__get__(None,A)
print("type:",type(unbm))
print(dir(unbm))
# print(unbm.__func__)#error
# print(unbm.__self__)#error
print(unbm.__call__)
print(unbm.__call__(a))
print('------------------')
class A(object):
    @classmethod
    def  ss(cls):
        pass
autobm = A.ss.__get__(None,A)

print(autobm.__self__)






