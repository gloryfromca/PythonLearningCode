class A(object):
	def __call__(self):
		return 'call'
class B(object):
	a = A()
b = B()
print(b.a)
print(b.a())

print('-------------')

import time
class Timeit(object):
    def __init__(self, func):
        self._wrapped = func
    def __call__(self, *args, **kws):
        start_time = time.time()
        result = self._wrapped(*args, **kws)
        print("elapsed time is %s " % (time.time() - start_time))
        return result
class A(object):
    @Timeit
    def func(self):
        time.sleep(1)
        return 'invoking method func'
if __name__ == '__main__':
    a = A()
    A.func(a)
    a.func(a)
    print('======')
    a.func()  # 在调用 func 函数的过程中其对应的 instance 并不会传递给 __call__ 方法，造成其 mehtod unbound
