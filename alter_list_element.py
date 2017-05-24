lists=[1,2,[],4]
lists[2]="aaa" #z这里更改的是lists元素

a=4
lists=[1,2,a,4]
a=6#z这里更改的是lists元素对应的值，因此list改变了


lists=[1,2,[],4]
s=lists[2]
s=5
#lists[2]list不变，因为不可变对象，重新赋值给s会导致重新将不可变对象5指向s

lists=[1,2,[],4]
s[2].append('asasa')

a=[ ]
lists=[1,2,a,4]
a.append('asasa')
#lists改变了
