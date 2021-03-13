from itertools import combinations
from collections import Counter
import os
import sys
from pathlib import Path
sys.path.append(str(Path(os.path.dirname(os.path.realpath(__file__))).parent))
print(sys.path)
from utils import primes

class Problem():
    def __init__(self, url):
        self.url = url

    def ana_solve(self):
        solution = 0
        primeList = [5,7,11,13,17,19,23]
        combos = combinations(primeList, 3)
        primeCombos = []
        for c in combos:
            s = sum(c)
            if primes.is_prime(s):
                primeCombos.append((c, s))
        counts = Counter([pc[1] for pc in primeCombos])
        bigC = []
        for c in counts:
            if counts[c] >= 4:
                bigC.append(c)
        candidates = []
        for pc in primeCombos:
            if pc[1] in bigC:
                candidates.append(pc)
                candidates.sort(key=lambda x: x[1])
        print(candidates)
        print('analytical solution = ', solution)

    def sim_solve(self):
        solution = 0
        print('simulation solution = ', solution)

    def prg_solve(self):
        solution = 0
        print('programmatic solution = ', solution)

if __name__ == '__main__':
    url = 'https://brilliant.org/daily-problems/grid-fill-16/'
    # define problem inputs
    p = Problem(url)
    p.ana_solve()
    p.sim_solve()
    p.prg_solve()


