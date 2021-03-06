import numpy as np
from math import factorial
from itertools import permutations

class Problem():
    def __init__(self, url):
        self.url = url

    def ana_solve(self):
        totalPossibilites = factorial(4)
        together = 2*2*3
        solution = together/totalPossibilites
        print('analytical solution = ', solution)

    def sim_solve(self):
        solution = 0
        nSim = 10**5
        possibilites = np.array([1,2,3,4])
        c = 0
        for i in range(nSim):
            np.random.shuffle(possibilites)
            idx1 = np.where(possibilites==1)[0]
            idx2 = np.where(possibilites==2)[0]
            if abs(idx1 - idx2)==1:
                c+=1
        solution = c/nSim
        print('simulation fraction = ', solution)

    def prg_solve(self):
        N = 4
        perms = list(permutations([*range(N)]))
        solution = sum([abs(row.index(1)-row.index(2)) == 1
                       for row in perms])/len(perms)
        print('programmatic solution = ', solution)

if __name__ == '__main__':
    url = 'https://brilliant.org/daily-problems/tree-diagram-2/'
    # define problem inputs
    p = Problem(url)
    p.ana_solve()
    p.sim_solve()
    p.prg_solve()
