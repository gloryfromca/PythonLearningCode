import re
a='ab cd ,ass   agg  , sr'
print(re.split(r'[\s\,]+',a))
# print(re.split(r'[\s\,]*',a))#会报警告
telephone1=re.compile(r'\d{3}\-\d{3,8}')

# telephone2=re.compile(r'\d{3}-\d{3,8}')
# telephone2=re.compile(r'(\d{3})-(\d{3,8})')
telephone2=re.compile(r'(\d{3})-(\d{3,8})$')

a1=telephone1.match('010-1343')
# a2=telephone2.match('010-13433111111233')#注意：此处被匹配上了
a2=telephone2.match('111-13433')
print(a1)
print(a2)
print(a1.groups())
print(a2.groups())
print('---------------------------')
a='ass|ss'
isemail=re.compile(r'\w+@\w+\.com')
isemail=re.compile(r'\w+@\w+\.c\om')
isemail=re.compile('\w+@\w+\.c\om')
isemail=re.compile(r'\w+@\w+\.c\\nm')#有转义,不然没有任何办法匹配换行符
isemail=re.compile(r'\w+@\w+\.c\nm')#有转义，可与上面调换位置看结果
isemail=re.compile('\w+@\w+\.c\nm')#有转义
print(r'\w+@\w+\.c\nm')#无转义
print(isemail.match(r'huizhang1995@gmail.com'))#无转义
print(isemail.match(r'huizhang1995@gmail.c\nm'))#无转义
print(isemail.match('huizhang1995@gmail.c\nm'))#有转义
print('---------------------------')
print(" ass\
	") #注意此处\的用法
a=\
1+3 #注意表达式也能这样用：忽略代码书写的换行，主要目的是在于把长行的代码分成两段
print(a)
print(r" ass\n")#原始字符串需要对引号进行转义，因为引号涉及字符串的开始结束
# print(r" ass"\n")#error
print('---------------------------')
