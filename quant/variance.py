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

# variance of number of heads in 10 flips
N = 100
result = []
for i in range(N):
    f = [random.randint(0, 1) for j in range(10)]
    result.append(sum(f))

result = np.var(np.array(result))  # ddof=9
print(result)

# variance of number of two consecutive heads in 10 flips
N = 100
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

result = np.var(np.array(result))  # ddof=9
print(result)

# price of stock increases with pI=1/3 and deacreases with pD=2/3
# variance of number that will increase of 5 independent stocks
N = 10000
result = []
sims = [[random.randint(0, 2) for j in range(5)] for i in range(N)]
result = [s.count(0) for s in sims]

print(len(result))
result = np.var(np.array(result))
print(result)


# price of stock increases with pI=1/3 and deacreases with pD=2/3
# variance of number that will increase of 5 independent stocks on 3 days
N = 1
result = []
sims = []
for i in range(N):
    days3 = [[random.randint(0,2) for j in range(5)] for day in range(3)]
    equals = days3[0]
    print(days3)
    truths = [1,1,1]
    for j in range(3):
        if equals !=0:
            truths[j] = 0
    for j in range(1,3):
        for k in range(3):
            if days3[j][k] != equals[k]:
                truths[k] = 0
    print(truths)
    c = sum(truths)
    sims.append(c)

result = sims
print(len(result))
result = np.var(np.array(result))
print(result)

