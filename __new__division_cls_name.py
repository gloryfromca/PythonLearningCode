class ReedSunMetaclass(type):
    def __new__(cls, name, bases, attrs):
        # 添加一个属性
        attrs['哈哈哈'] = True
        print(cls)
        print(name)
        return type.__new__(cls, name, bases, attrs)
class asd(dict,metaclass=ReedSunMetaclass):
    pass
s=asd()