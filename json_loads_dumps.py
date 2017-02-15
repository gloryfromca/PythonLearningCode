import json
b=['io',8]
a=json.dumps(b)
d=json.loads(a)
print(a)
print(type(a))
print(d)
print(type(d))
with open ('a.txt','w') as y:
    json.dump(a,y)
with open('a.txt','r') as y:
    c=json.load(y)
print(c)
print('--------------')
d=dict(name='Bob',score=80)
print(json.dumps(d))
print(type(json.dumps(d)))
#json类型都是str类型
s='{"age":20,"score":88}'
print(json.loads(s))
print(type(json.loads(s)))
# k="{"age":20,"score":88}"#错误的字符串书写
k="{\"age\":20,\"score\":88}"
print(k)
print(json.loads(k))
print(type(json.loads(k)))
