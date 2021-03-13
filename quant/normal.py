from math import log
# point of intersection between two normal curves
# from first principles
def interesect2normals(m1, s1, m2, s2):
    K = s1/s2*(log(s1/s2))**0.5
    x = (K*m1-m2)/(K-1)
    return x

# programmatic

# tables

# results
m1, s1 = 3, 1.5
m2, s2 = 4, 2
xfp = interesect2normals(m1,s1,m2,s2)



print('intersection from first principes = ', xfp)


