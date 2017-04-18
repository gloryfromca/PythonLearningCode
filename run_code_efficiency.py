import cProfile
import random
def f1(lIn):
    return sorted(lIn)
sIn = [random.random() for i in range(100000)]
sIn1 = [random.random() for i in range(10000)]
cProfile.run('f1(sIn)')
cProfile.run('f1(sIn1)')
