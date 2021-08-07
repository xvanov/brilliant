import numpy as np

class Problem():
    def __init__(self, url, args):
        self.url = url
        self.args = args
        self.pU = args['pU']
        self.pD = args['pD']
        self.pS = args['pS']
        self.d = args['d']
        self.c = args['c']
        self.As = args['As']

    def sim_solve(self):
        solution = 0
        N = 10000
        V = []
        for n in range(N):
            Vc = 0
            for i in range(self.d):
                dc = self.As*np.random.choice(np.array([self.c,-self.c,0]), p=[self.pU, self.pD,self.pS])
                Vc += dc
            V.append(Vc)
        solution = sum(V)/N

        print('simulation solution = ', solution)

    def prg_solve(self):
        solution = 0
        print('programmatic solution = ', solution)

    def ana_solve(self):
        solution = 0
        solution = self.d*self.As*(self.pU*self.c - self.pD*self.c)
        print('analytical solution = ', solution)

if __name__ == '__main__':
    url = 'https://brilliant.org/daily-problems/trading-brillcoins/'

    # define problem inputs
    args = {'pU': 0.75,
            'pD': 3/16,
            'pS': 1/16,
            'c': 1,
            'As': 16,
            'd': 7}
    p = Problem(url, args)
    # solve
    p.sim_solve()
    p.prg_solve()
    p.ana_solve()

