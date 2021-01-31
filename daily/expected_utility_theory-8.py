import numpy as np
from math import log
def mU_A(x,w):
    return 0.5*log(w+x) + 0.5*log(w-1) - log(w)
def mU_B(x,w):
    return 0.5*(w+x)**0.5 + 0.5*(w-1)**0.5 - w**0.5

if __name__ == '__main__':
    w = 100
    for x in np.linspace(0,100,10000000):
        a = mU_A(x,w)
        b = mU_B(x,w)
        if abs(a) <= 0.000001:
            print('A ', x)
        if abs(b) <= 0.000001:
            print('B', x)
