import sqlalchemy
a=3
b=4
local1=locals()
print(local1)
print('-----------')
global1 =globals()
print(global1)
print('-----------')
local2 = locals()
print(local2)
local3 = locals()
print(local3)
global2=globals()
print(global2)
var=vars()

var_list=list(var.items()) 
global_list=list(global2.items())

other=[ i for i in list(var.items()) if i not in list(global2.items())]
print(other)
