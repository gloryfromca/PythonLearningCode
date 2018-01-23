#ORM:object relational mapping 对象-关系映射
#把关系数据库的一行映射为一个对象，也就是一个类对应一个表
#ORM框架所有的类只能动态定义


# 定义Field(定义域：元类遇到Field的方法或属性时即进行修改）
class Field(object):

    def __init__(self, name, column_type):  # 字段名和字段类型
        self.name = name
        self.column_type = column_type

    # 当用print打印输出的时候，python会调用他的str方法
    # 在这里是输出<类的名字，实例的name参数(定义实例时输入)>
    # 在ModelMetaclass中会用到
    def __str__(self):
        return "<%s:%s>" % (self.__class__.__name__, self. name)  # __class__获取对象的类，__name__取得类名
        #return "<%s:%s>" % (self.__class__.__name__, self)#打印self就是打印对象，就会调用__str__函数，然后发生循环调用。

    #def __str__(self):#尝试去掉，看看打印效果！！！！！！
        #return "<%s:%s>" % (self.__class__.__name__, self. name)  
        #return "<%s:%s>" % (self.__class__.__name__, self)


# 进一步定义各种类型的Field
class StringField(Field):

    def __init__(self, name):
        # super(type[, object-or-type])  返回type的父类对象
        # super().__init()的作用是调用父类的init函数
        # varchar(100)和bigint都是sql中的一些数据类型
        super(StringField, self).__init__('%s1223'%name, "varchar(100)")  #此处的name是类的实例属性

class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, "bigint")


# 编写ModelMetaclass
class ModelMetaclass(type):

    # __new__方法接受的参数依次是：
    # 1.当前准备创建的类的对象（cls）
    # 2.类的名字（name）
    # 3.类继承的父类集合(bases)
    # 4.类的方法集合(attrs)
    print('----我这个时候被读，只出现一次，只有新建立类的时候才会出现print(attrs)结果----')
    def __new__(cls, name, bases, attrs):
        # 如果说新创建的类的名字是Model，那直接返回不做修改
        print('-----------------------')
        print(attrs)
        print('-----------------------')
        if name == "Model":
            return type.__new__(cls, name, bases, attrs)
        print("Found model:%s" % name)
        mappings = dict()
        for k, v in attrs.items():#attrs.items()调用是User（）的类属性，四个对应而不是下面的五个对应
            if isinstance(v, Field):
                print("Found mappings:%s ==> %s" % (k, v))  # 找到映射， 这里用到上面的__str__
                mappings[k] = v
                #print(str(v))#没什么卵用，和下面的结果一样
                print(v)
                print('=============开始============')
                print(attrs.items())
                print('上下打印的结果不同，调用items以dict的形式返回')
                print(attrs)
                print('=============结束==============')
                #print()
            # 结合之前，即把之前在方法集合中的零散的映射删除，
            # 把它们从方法集合中挑出，组成一个大方法__mappings__
            # 把__mappings__添加到方法集合attrs中
        for k in mappings.keys():
                 attrs.pop(k)

        attrs["__mappings__"] = mappings

        attrs["asd"]='as21fddgafd'
        attrs["email"]='as2134344444d'#会覆盖前面的User（）中传进来的对应
        attrs["__table__"] = name # 1添加表名，假设表名与类名一致
        return type.__new__(cls, name, bases, attrs)
print('----------ORZ-------------')
print(ModelMetaclass)
print ('读取完ModelMetaclass,并建立一个对象，上面的是类在内存被创建为对象地址')
print('----------ORZ-------------')

# 编写Model基类继承自dict中，这样可以使用一些dict的方法
class Model(dict, metaclass=ModelMetaclass):
    print('--------读取到这里是调用了model,print一下，然后开始创建一个class的对象--------')#万物皆对象，class也是！！！
    print('------新建Model class的类需要用到metaclass，因此会出现print(attrs)结果------')
    #print(Model) 无效果因为还没被创建
    def __init__(self,  **kw):
        # 调用父类，即dict的初始化方法
        super(Model, self).__init__(**kw)

    # 让获取key的值不仅仅可以d[k]，也可以d.k
    def __getattr__(self, key):#self.name在外面的属性中没有找到，才到__getattr__里面找到
        try:
            return self[key]
            #这里的key被执行的时候被认为是字符串，但是我们自己写必须加''才被认为是字符串！！！！！
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    # 允许动态设置key的值，不仅仅可以d[k]，也可以d.k
    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        # 在所有映射中迭代
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append("?")
            args.append(getattr(self, k, None))
            print(k,':')
            print('%s:'%k)
            print(getattr(self, k, None))
        sql = "insert into %s (%s) values (%s)" % (self.__table__, "1111".join(fields), ",".join(params))
        print("SQL: %s" % sql)
        print("ARGS: %s" % str(args))
print('----------ORZ-------------')
print(Model)
print ('读取完Model,并建立一个对象，上面的是类在内存被创建为对象地址')
print('----------ORZ-------------')
# 这样一个简单的ORM就写完了


# 下面实际操作一下，先定义个User类来对应数据库的表User
class User(Model):
    # 定义类的属性到列的映射
    print('--------读取到这里是调用了User,print一下，然后创建了一个class的对象--------')#万物皆对象，class也是！！！
    print('------新建User class的类需要用到metaclass，因此会出现print(attrs)结果------')
    id = IntegerField("id111")#建立了四个class的实例，是类的属性；与下面User（）中传入的不冲突
    name = StringField("username789")#转到metaclass.__new__的时候，应该是这四个方法或者说属性 
    email = StringField("email")#等号前面是K，后面是V（类的属性：名称到内容）
    password = StringField("password")#括号里面的是创建类的实例的name参数，和前面的实例名重合是偶然
    #password = "password"#类的属性

print('----------ORZ-------------')
print(User)
print ('读取完User,并建立一个对象，上面的是类在内存被创建为对象地址')
print('----------ORZ-------------')



# 创建一个实例
u = User(id=12345, name="ReedSun", email="sunhongzhao@foxmail.com", password="nicaicai",newkey="注意我被加进去，作为key-value对应关系（本类继承了dict,，可以传实例属性）。是实例的属性，不是类的属性")
u.id='asda'
u.save()
print('-----------------------')
print (u.id)#本来是访问类属性的方法。原来id指向类属性，后来被放到__mappings__,然后删除；没有类属性，通过__getattr__寻找，发现要求返回self[key]（dict的访问），然后返回id最为key对应的value
#print (u[id])#error
print(u.password)
print (u['password'])#父类model继承了dict的方法
print(u.asd)
print(u['newkey'])
print(u.newkey)
print (u.__mappings__['password'])
print (u.__mappings__)
print (u.__mappings__.items())
print (u.__table__)
#print (u['__table__']) 报error，因为该形式以key访问mappings，而里面却是没有__table__的key



 

