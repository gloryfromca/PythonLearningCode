print(object.__class__)
print(type.__class__)

class g(dict):
    pass
class h(g):
    pass
print(g.__class__)
print(h.__class__)
print(g().__class__)
print(h().__class__)

g = "z" 
print(g.__class__)
print(g.__class__.__class__)
