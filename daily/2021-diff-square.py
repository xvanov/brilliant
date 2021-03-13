from matplotlib import pyplot as plt
import numpy as np

class Problem():
    def __init__(self, url):
        self.url = url

    def ana_solve(self):
        solution = 0
        z = 2021
        print('analytical solution = ', solution)

    def sim_solve(self):
        solution = []
        n = 10**5
        z = 2021
        diffs = []
        for i in range(n):
            sqi = i**2
            s = (z+sqi)
            ss = s**0.5
            d = ss - int(ss)
            if d == 0:
                solution.append((i,ss))
            diffs.append(d)
        print('simulation solution = ', solution)
        x = np.arange(0,n)
        y = np.array(diffs)
        plt.plot(x,y)
        plt.show()
    def prg_solve(self):
        solution = 0
        print('programmatic solution = ', solution)

if __name__ == '__main__':
    url = 'https://brilliant.org/daily-problems/2021-diff-square/'
    # define problem inputs
    p = Problem(url)
    p.ana_solve()
    p.sim_solve()
    p.prg_solve()


