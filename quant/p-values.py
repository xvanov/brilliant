# imports
import numpy as np
from itertools import combinations
import random

# belief = stock goes up with 1/2 and down with 1/2, 
# obeservation = goes up 8 days and down 2 days in 14 day window 
# is the belief flawed at 5% signinficant?

# find probability of getting 8 days up and 2 days down (or more extreme)!

# analytical
N = 10
possible = [*range(N)]
combos = [len(list(combinations(possible, i))) for i in range(N+1)]
u8d2 = combos[2]+combos[1]+combos[0]
total = 2**N
probOccur = 1/total
p_u8d2 = u8d2*probOccur

# simulation
K = 10**5
p = 1/2
c = 0
for i in range(K):
    r = [random.randint(0,1) for i in range(N)]
    if sum(r) >= 8:
        c +=1
pSim = c/K
print('number of days =', N)
print('all counts = ', combos)
print('up 8 down 2 = ', u8d2)
print('check total count = ', sum(combos))
print('2^N = ', total)
print('probablilty of occuring = ', p_u8d2)
print('sim prob of 8 up and 2 down = ', pSim)
