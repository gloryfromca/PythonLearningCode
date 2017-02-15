def fact(n):
    '''
>>> a=fact(1)
>>> print(a)
1
>>> a=fact(-1)
Traceback (most recent call last):
  ...
ValueError
>>> a=fact(2)
>>> print(a)
2
    '''

    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()