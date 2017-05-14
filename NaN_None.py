from numpy import NaN
from pandas import Series, DataFrame
import numpy as np
print(type(None),type(NaN))
print({None:1, NaN:2})
print(np.array([1,None]).dtype ,np.array([1,NaN]).dtype ,np.array([1,2]).dtype  )
print('------------------')
s = Series([None, NaN, 'a'])
d1=s.map({NaN:2,'None':1,'a':'a'})
print(d1)
d2=s.map({'None':1,NaN:3,'a':'a'})
print(d2)
print('------------------')
print(Series([1.0, None]))
print('------------------')
print((1, NaN) == (1, NaN),NaN == NaN)
print('------------------')
print(np.array([1,None]) == np.array([1,None]),type(np.array([1,None]) == np.array([1,None])))


