def cssssss(*ccc, **sss):
    print(ccc)
    print(sss)
cssssss(*{'1':342,'2':3287456})
print('=====')
cssssss(*{1:342,2:3287456})
print('=====')
cssssss(**{'1':342,'2':3287456})
print('=====')
cssssss(**{1:342,2:3287456})#报错原因：数字不能做变量名