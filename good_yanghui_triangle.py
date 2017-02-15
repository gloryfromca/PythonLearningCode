def triangles():
    L = [1]
    while True:
        yield L
        L.append(0);
        L = [L[i-1] + L[i] for i in range(len(L))]
        #线把所有结果放在一个list对象中，再由L指向该地址；之前我是每出一个结果就放到L中，结果后面还要用到的
        #变量被覆盖掉了
#      1
#(0)  1  1  (0)
#    1  2  1      
