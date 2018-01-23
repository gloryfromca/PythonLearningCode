def get_instance(x):
 	return eval(x)
 # 返回一个值，有很好的效果

def get_instance(x):
 	exec('sss={}'.format(x))
	return locals()['sss']
#format之后exec执行，赋值给sss，然后用locals()取用。

#以上两者都能够实现将对象的字符串形式转变为Python的实际对象。

def get_instance(x):
	exec('sss={}'.format(x))
	print(locals())
	return sss
#错误原因：没有过语法分析。
#在exec执行之前，sss变量在全局和本地都没有定义过，因此报错。
#但是exec执行之后会被写进locals()本地变量集合中。


def get__():
  exec('sasaas=(1,2)')
# return locals()['sasaas'], type(locals()['sasaas'])
# 注意传入的方式和下面函数的区别

def get_instance(x):
  exec('sss=x')
  return locals()['sss']
#无转换为对象的效果，还是一个字符串。
#因为在执行的时候寻找变量x（这里找变量的原则就是本地没有找全局）。发现是个字符串，结果sss就成了一个字符串


def get_instance(x):
  exec(x)
  return x
#无转换为对象的效果，因为执行根本没有产生本地或者全局的变量
#最后的返回就是传进来的参数

#上面x的情景类似于
def get_instance(x):
  11
  print(locals())
  return x
#中11的情形

def get_instance(x):
  l = {}
  exec('sss=x',locals(), l)
  return l['sss']
#无转换为对象的效果,必须format进去才能去掉参数x作为字符串的地位
