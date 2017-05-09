s=[1,2,3]
n=0
for i in s[n:]:

  if n==1:
    n=2
  if n==2:
    n=1

  print(i)

d=s[n:]
for i in d:
  d=[6,6,6]

  print(i)


for i in s[n:]:
  try:
    s.remove(3)
  except ValueError as e:
    pass
  print(s)
  print(i)


for i in s:
  try:
    s.remove(3)
  except ValueError as e:
    pass
  print(s)
  print(i)

s1=[1,2,3,3]
ss=0
print(s1[ss:ss+1] == s1[ss])
print(s1[ss])#element 
print(s1[ss:ss])#list
print(s1[ss:ss+1])#list

print(s1[:2])

s1=[1,2,3,3]

for i in s1:
  s1.remove(i)
  print(i)

#访问in后的对象按照索引递增的规则，擅自更改目前索引之前的索引会跳过一部分元素



