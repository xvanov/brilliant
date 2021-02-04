import numpy as np
import random

sample = np.array([2.74, 1.23, 2.63, 2.22, 3, 1.98])
v1 = np.var(sample)
sample2 = sample*2
v2 = np.var(sample2)
sample3 = sample + 2
v3 = np.var(sample3)
print(v1, v2, v1*4, v1*4 == v2)
print(v1,v3,v1==v3)

def discrete_var(l,p):
    v = 0
    e = 0
    for i in range(len(l)):
        e += l[i]*p[i]
        v += l[i]**2*p[i]
    v -= e**2
    return v

sample4 = list(sample)
N = len(sample4)
p4 = [1/N]*N

v4 = discrete_var(sample4, p4)
print(v1,v4, v1==v4)

sample5 = [1,2,3,4,5,6]
N = len(sample5)
p5 = [1/N]*N

v5 = np.var(np.array(sample5))
v5m = discrete_var(sample5,p5)
print(v5,v5m)

