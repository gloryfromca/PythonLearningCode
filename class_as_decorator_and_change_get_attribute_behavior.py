class _Missing(object):
    def __repr__(self):
        return 'no value'

    def __reduce__(self):
        return '_missing'


_missing = _Missing()


class cached_property(object):
    def __init__(self, func, name=None, doc=None):
        self.__name__ = name or func.__name__
        self.__module__ = func.__module__
        self.__doc__ = doc or func.__doc__
        self.func = func
        print('func is:',func)

    def __get__(self, obj, type=None):#obj就是对应的Foo实例f
        if obj is None:
            return self
        value = obj.__dict__.get(self.__name__, _missing)
        if value is _missing:

            value = self.func(obj)
            print('object is:',obj)
            print(isinstance(obj,Foo))
            print('value :', value)
            print('self.__name__ :',self.__name__)

            obj.__dict__[self.__name__] = value
        return value


class Foo(object):
    @cached_property
    def foo(self):
        print ('first calculate')
        result = 'this is result'
        return result


f = Foo()

print (f.foo )  # first calculate this is result
print('--------------')
print (f.foo )# this is result
print('--------------')
print(f.__dict__)
