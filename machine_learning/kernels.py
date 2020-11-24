import numpy as np
import math

class Kernels():
    def __init__(self):
        pass

    def linear(self, u, v):
        return np.dot(u,v)

    def polynomial(self, u, v, r, n):
        return (np.dot(u,v) + r)**n

    def radial_basis(self, u, v, sigma):
        return math.exp(-(np.linalg.norm(u - v))**2/(2*sigma**2))

    def laplacian(self, u, v):
        return math.exp(-np.linalg.norm(u - v))

if __name__ == '__main__':
    k = Kernels()
    u = np.array([32, 140])
    v = np.array([15, 90])
    r = 1
    n = 2
    sigma = 100
    linear_diff = k.linear(u,v)
    polynom_diff = k.polynomial(u,v,r,n)
    rb_diff = k.radial_basis(u,v,sigma)
    print(linear_diff, polynom_diff, rb_diff)
