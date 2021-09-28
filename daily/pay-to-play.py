import random

class Problem():
    def __init__(self, url):
        self.url = url

    def ana_solve(self):
        solution = 0
        const = (1+6)/2
        geome = 1/6
        solution = const * 1/(1-geome)
        print('analytical solution = ', solution)

    def sim_solve(self):
        solution = 0
        N = 10000
        sims = []
        for i in range(N):
            r = 0
            tmp = 0
            while r == 6 or r == 0:
                r = random.randint(1,6)
                tmp +=r
            sims.append(tmp)
        solution = sum(sims)/N
        print('simulation solution = ', solution)

    def prg_solve(self):
        solution = 0
        print('programmatic solution = ', solution)

if __name__ == '__main__':
    url = 'https://brilliant.org/daily-problems/pay-to-play/'
    # define problem inputs
    p = Problem(url)
    p.ana_solve()
    p.sim_solve()
    p.prg_solve()


