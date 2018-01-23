class a(dict):
	sd={'a':'as','b':'ss'}
	adsa={'c':'op','d':'er'}
s=a(sd=1222222,adsa=34545)
print(s.sd['a'])
print(s['sd'])



class Field(object):

    def __init__(self, name): 
        self.name = name
    def __str__(self):
        return "<%s:%s>" % (self.__class__.__name__, self. name) 
class User(dict):
    # 定义类的属性到列的映射
    id = int()
    #name = Field("username789") 
    email = Field("email")
    password = Field("password")


u = User(id=12345, name="ReedSun", email="sunhongzhao@foxmail.com", password="nicaicai")
print(u.id)
print(u['id'])
#print(u.name)
print(u['name'])