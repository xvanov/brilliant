import numpy as np
from itertools import permutations
from itertools import combinations

class Problem():
    def __init__(self, url):
        self.url = url

    def ana_solve(self):
        solution = 0
        print('analytical solution = ', solution)

    def sim_solve(self):
        solution = 0
        print('simulation solution = ', solution)

    def prg_solve(self):
        solution = 0
        N = 4
        c2 = 11
        c3 = 9
        c4 = 36
        c5 = 1
        perms = list(permutations(permutations(range(1,N+1)),4))
        print(len(perms))
        sols = []
        for row in perms:
            if row[3][3] != c5: continue
            if row[0][0] + row[0][1] + row[0][2] + row[1][0] + row[2][0] != c2: continue
            if row[1][1] + row[2][1] + row[2][2] != c3: continue
            if row[1][3]*row[2][3]*row[3][1]*row[3][2] !=c4: continue
            check_final = True
            for i in range(0,N-1):
                collist = [row[0][i], row[1][i], row[2][i], row[3][i]]
                if (1 not in collist) or (2 not in collist) or (3 not in collist) or (4 not in collist):
                    check_final = False
                    break
            if not check_final: continue
            sols.append(row)
        solution = sols
        print('programmatic solution = ', len(solution))
        for s in solution:
            print('\n')
            for z in s:
                print(f"{z}")

if __name__ == '__main__':
    url = 'https://brilliant.org/daily-problems/calcdoku-18/'
    # define problem inputs
    p = Problem(url)
    p.ana_solve()
    p.sim_solve()
    p.prg_solve()


