class Sreen(object):
    def __init__(self,weight,height,resolution=1):
        self.__weight=weight#外部属性赋值给内部private变量
        self.__height=height
        self.__resolution=resolution
    weight=1223#为类增加属性，但是因为优先考虑同名方法转变成的属性，访问不到
    __weight=1234#私人变量，在内部使用
    height=1237
    __resolution=0 #为private变量赋值，但不是给类增加属性，在内部使用
    __height=0
    resolution=123
    @property
    def weight(self):
        return self.__weight
    @weight.setter
    def  weight(self,jinlaide):
        if jinlaide<190 and jinlaide>0:
            self.__weight=jinlaide
        return None
    @property
    def resolution(self):
        return self.__resolution
a=Sreen(234,538)
print(a.weight)
a.weight=140
print(a.weight)
a.weight=100
print(a.weight)
a.weight=400
print(a.weight)#未改变，是100
print('-------------------')
print(a.height)
print(a.resolution)#可能优先考虑方法转变成的属性，尽管还有一个设置resolution=123
print('-------------------')
print(a._Sreen__height) 
a._Sreen__height=15
print(a._Sreen__height)
print('-------------------')
print(a.resolution)
#a.resolution='不及格'
#print(a.resolution)
print('===================')
#a=Sreen(180，2，3)
a.weight=140
print(a.weight)
a.weight=100
print(a.weight)
a.height=400
print(a.weight)#未改变，是100
print('-------------------')
print(a._Sreen__height) 
a._Sreen__height=15
print(a._Sreen__height)
print('-------------------')
print(a.resolution)
a.resolution='不及格'
print(a.resolution)




