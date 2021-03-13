import numpy as np
import random


def discrete_var(listOfNumbers, listOfProbabilities):
    '''
    computes variance from list and probabilites (2 lists of the same size)
    '''
    v = 0
    e = 0

    for number, probability in zip(listOfNumbers, listOfProbabilities):
        e += number*probability
        v += number**2*probability
    v -= e**2
    return v

'''
sample = np.array([2.74, 1.23, 2.63, 2.22, 3, 1.98])
v1 = np.var(sample)
sample2 = sample*2
v2 = np.var(sample2)
sample3 = sample + 2
v3 = np.var(sample3)
print(v1, v2, v1*4, v1*4 == v2)
print(v1, v3, v1 == v3)

sample4 = list(sample)
N = len(sample4)
p4 = [1/N]*N

v4 = discrete_var(sample4, p4)
print(v1, v4, v1 == v4)

sample5 = [1, 2, 3, 4, 5, 6]
N = len(sample5)
p5 = [1/N]*N

v5 = np.var(np.array(sample5))
v5m = discrete_var(sample5, p5)
print(v5, v5m)
'''

'''
N = 100
sumTheResult = []
twoTimesValue = []
for i in range(N):
    q = random.randint(1, 6)
    s = random.randint(1, 6)
    sumTheResult.append(q + s)
    twoTimesValue.append(2 * q)

v6 = np.var(np.array(sumTheResult))
v6_2 = np.var(np.array(twoTimesValue))
print(v6, v6_2)
'''

'''
N = 100
result = []
for i in range(N):
    f = random.randint(0, 1)
    if f == 0:
        q = random.randint(1, 6)
    else:
        q = random.randint(1, 4)

    result.append(q)


v7 = np.var(np.array(result))
print(v7)
'''

# variance of number of heads in 10 flips
'''
N = 100
result = []
for i in range(N):
    f = [random.randint(0, 1) for j in range(10)]
    result.append(sum(f))

result = np.var(np.array(result))  # ddof=9
print(result)
'''

# variance of number of two consecutive heads in 10 flips
'''
N = 10**4
result = []
for i in range(N):
    f = [random.randint(0, 1) for j in range(10)]
    n = 0
    prev = 0
    for v in f:
        if v == 1 and prev == 1:
            n += 1
        prev = v
    result.append(n)

result = np.var(np.array(result))
print('variance of 2 consecutive heads in 10 flips = ', result)
'''
# price of stock increases with pI=1/3 and deacreases with pD=2/3
# variance of number that will increase of 5 independent stocks
'''
N = 10000
result = []
sims = [[random.randint(0, 2) for j in range(5)] for i in range(N)]
result = [s.count(0) for s in sims]

result = np.var(np.array(result))
print(result)
'''
# price of stock increases with pI=1/3 and deacreases with pD=2/3
# variance of number that will increase of 5 independent stocks on 3 days
'''
N = 10**2
result = []
sims = []
for i in range(N):
    days3 = [[random.randint(0,2) for j in range(5)] for day in range(3)]
    equals = days3[0]
    #print(days3)
    truths = [1,1,1,1,1]
    for j in range(3):
        for k in range(5):
            if days3[j][k] != 0:
                truths[k] = 0
    #print(truths)
    #print(sum(truths))
    c = sum(truths)
    sims.append(c)

print('Number of sims: ', len(sims))
result = np.var(np.array(sims))
print('Simulation Variance = ', result)

# analytical sol
nDays = 3
incProb = 1/3
nStocks = 5
inc3Days = incProb**nDays
binomialVar = nStocks*(inc3Days)*(1-inc3Days)
print('Analytical Variance = ', binomialVar)
'''

# minimum number of stocks to hold such that the variance is at least 1
'''
simVar = 0
result = []
simNStocks = 5
nDays = 3
while simVar < 1:
    sims = []
    N = 10**2
    for i in range(N):
        days3 = [[random.randint(0,2) for j in range(simNStocks)] for day in range(nDays)]
        truths = [1]*simNStocks
        for j in range(nDays):
            for k in range(simNStocks):
                if days3[j][k] != 0:
                    truths[k] = 0
        c = sum(truths)
        sims.append(c)

    simVar = np.var(np.array(sims))
    simNStocks +=1

print('Simulation variance = ', simVar)
print('Simulation number of stocks = ', simNStocks)

# analytical sol
nDays = 3
incProb = 1/3
nStocks = 5
inc3Days = incProb**nDays
binomialVar = 1
nStocks = binomialVar/((inc3Days)*(1-inc3Days))
print('Analytical number of stocks = ', nStocks)
'''

# variance of number of 2 heads occuring
'''
# sim
N = 10**6
sims = []
for i in range(N):
    flips = [random.randint(0, 1) for j in range(10)]
    n = 0
    prev = 0
    for v in flips:
        if v == 1 and prev == 1:
            n += 1
        prev = v
    sims.append(n)

simVar = np.var(np.array(sims))
simMean = np.mean(np.array(sims))
# analytic
p = 1/4
n = 9
binMean = n*p
binVar = n*p - (n*p)**2 + (n-1)*(n-2)*(p**2) + 2*(n-1)*p*1/2


# print
print('X = indicator variable for count of 2 consecutive heads in 10 throws')
print('simMean = ', simMean)
print('anaMean = ', binMean)
print('simVar = ', simVar)
print('anaVar = ', binVar)
'''
# expected value of indicator variable squared
# X = indicator variable, E(X) = p
# since an indicator variable X takes only values 0 v 1 X = X^2
# E(X) = E(X^2)

# 1 stock or 25 stocks

# problem
s1 = 750
n1 = 1
m1 = 0.03

s2 = 30
n2 = 25
m2 = 0.03
std2 = 0.015

# find std1

# analytical
std1_ana = (n2*s2*std2**2)**0.5/s2
print('analytic combined standard deviation = ', std1_ana)

# simulation
N = 10**4

stds = []
for i in range(N):
    samples = np.random.normal(m2*s2, scale=std2*s2, size=n2)
    stds.append(np.std(samples))

std1_sim = np.mean(stds)/s2
print('simulation combined standard deviation = ', std1_sim)
# programmatic

std1_prg = 0
print('programmatic combined standard deviation = ', std1_prg)
