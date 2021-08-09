from random import randint
class Problem():
    def __init__(self, url, N1, N2):
        self.url = url
        self.N1 = N1
        self.N2 = N2

    def ana_solve(self):
        solution = 0
        print('analytical solution = ', solution)

    def sim_solve(self):
        solution = 0
        N = 10000
        w = 0
        for i in range(N):
            s1 = [randint(0,1) for j in range(self.N1)]
            s2 = [randint(0,1) for j in range(self.N2)]
            if sum(s2) > sum(s1):
                w += 1
        solution = w/N
        print('simulation solution = ', solution)

    def prg_solve(self):
        solution = 0
        print('programmatic solution = ', solution)

if __name__ == '__main__':
    url = 'https://brilliant.org/daily-problems/one-more-flip/'
    # define problem inputs
    N1 = 10
    N2 = 11
    p = Problem(url, N1, N2)
    p.ana_solve()
    p.sim_solve()
    p.prg_solve()


