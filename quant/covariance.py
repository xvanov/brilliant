import numpy as np

def covarfn(a, b, av_a, av_b):
    cov = 0

    for i in range(0, len(a)):
        cov += (a[i] - av_a) * (b[i] - av_b)
    return (cov / (len(a)))  # divide by N-1

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
