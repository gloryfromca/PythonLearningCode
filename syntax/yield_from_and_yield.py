def B():
    yield "1"
    yield "2"

def C():
    yield "3"
    yield "4"

def A():
    yield from B()
    yield from C()

def all():
    yield from A()

a = all()

for i in a:
    print(i)