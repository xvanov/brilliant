import random
from numpy import mean

def coat_sim(N):
    people = list(range(N))
    coats = list(range(N))
    random.shuffle(coats)
    matches = 0
    for i in range(N):
        if coats[i] == people[i]:
            matches+=1
    return matches

if __name__ == '__main__':
    N = 100
    S = 10000
    sims = []
    for i in range(S):
        m = coat_sim(N)
        sims.append(m)
    print(mean(sims))

