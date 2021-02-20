import random
import numpy as np
from itertools import product

class Problem():
    def __init__(self, url):
        self.url = url

    def solve(self):
        print(['Y', 'B', 'R'])
        anaSol = self.solve_analytical()
        simSol = self.solve_sim()
        print(f"analytical: {anaSol}, {anaSol/anaSol.sum()}")
        print(f"simulation: {simSol}, {simSol/simSol.sum()}")

    def solve_analytical(self):
        red, blue, yellow = 0, 0, 0
        for moves in product((1, -1, 1j, -1j), repeat=4):
            z = sum(moves)
            if abs(z - 1) <= 1:
                red += 1
            elif abs(z) <= 2:
                blue += 1
            else:
                yellow += 1
        solution = np.array([yellow, blue, red])
        return solution

    def solve_sim(self):
        solution = 0
        N = 100000
        coords = [self.one_run() for i in range(N)]
        regions = [0, 0, 0] # Y, B, R
        for c in coords:
            if abs(c[0])+abs(c[1]) >= 3:
                regions[0] += 1
            elif c[1] >= 1:
                regions[2] += 1
            elif c[0] == 0 and c[1] == 0:
                regions[2] +=1
            else:
                regions[1] +=1
        assert sum(regions) == N
        solution = np.array(regions)
        return solution

    def one_run(self):
        moves = [('V', 1), ('V', -1), ('H', 1), ('H', -1)]
        numberMoves = 4
        robotMoves = [random.choice(moves) for i in range(numberMoves)]
        x, y = (0,0)
        for m in robotMoves:
            if m[0] == 'H':
                x+=m[1]
            if m[0] == 'V':
                y+=m[1]
        coord = (x,y)
        return coord
if __name__ == '__main__':
    url = 'https://brilliant.org/daily-problems/robot-roaming/'
    # define problem inputs
    p = Problem(url)
    p.solve()
