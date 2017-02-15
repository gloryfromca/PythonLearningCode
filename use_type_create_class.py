class ReedSun(ShuaiGe):
    shuai = True
    def test(x):
        return x+2
# 就等价于
type("ReedSun", (ShuaiGe,), {"shuai":True, "test":lambda x: x+2})
# （属性和方法本质上都是方法）