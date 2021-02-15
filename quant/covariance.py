import numpy as np
import random

def covarfn(a, b, av_a, av_b):
    cov = 0

    for i in range(0, len(a)):
        cov += (a[i] - av_a) * (b[i] - av_b)
    return (cov / (len(a)))  # divide by N-1

def cov_sum(a,b):
    var_ab = np.var(a) + np.var(b) + 2*np.cov(a,b,bias=True)
    return var_ab

def my_npcov(a,b):
    a_m = np.mean(a)
    b_m = np.mean(b)
    cov = np.dot((a - a_m), (b-b_m))/a.size
    return cov


def covariance(X,Y):
    '''
    covariance assuming uniform distribution of X and Y
    '''
    N = len(X)
    ev_x  = 0
    ev_y = 0
    ev_xy = 0

    for i in range(len(X)):
        x = X[i]
        y = Y[i]
        ev_xy += x*y*1/N
        ev_x += x/N
        ev_y += y/N

    cov = ev_xy - ev_x*ev_y
    return cov

X = [1,2,3,4,5]
Y = [1/x for x in X]

ev_X = sum(X)/len(X)
ev_Y = sum(Y)/len(Y)

npcov = np.cov(np.stack((X,Y),axis=0))
cov = covariance(X,Y)
ocov = covarfn(X,Y,ev_X,ev_Y)
print('my covariance', cov)
print('np covariance', npcov)
print('other covariance', ocov)


N = 10000
rolls = [random.randint(1,7) for i in range(N)]
rolls = [*range(1,7)]
rolls2 = [r**2 for r in rolls]
cov = covariance(rolls, rolls2)
print('my covariance', cov)

X = np.arange(1,7)
X2 = X**2
npcov = np.cov(X2, X, bias=True)
print(npcov)


mycov = my_npcov(X2,X)
print(mycov)

cov_ab = cov_sum(X2,X)
print('sum of x2 and x vars', cov_ab)

N = 100000

stks = []
for i in range(N):
    c = random.choice([1,2,3])
    stk = [1 if random.choice([1,2,3])==3 else 0 for i in range(10)]
    U = sum(stk)
    D = len(stk) - U
    stks.append((U,D))
U = [p[0] for p in stks]
D = [p[1] for p in stks]
stk_cov = np.cov(np.array(U), np.array(D), bias=True)

print(stk_cov)



