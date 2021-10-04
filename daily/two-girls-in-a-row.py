import random
class Problem():
    def __init__(self, url, B):
        self.B = B
        self.url = url

    def ana_solve(self):
        solution = 81/4 # 81 pairs each with 0.25 probability 
        print('analytical solution = ', solution)

    def sim_solve(self):
        solution = 0
        N = 10000
        consecutivecounts = []
        for i in range(N):
            pb = 99
            consecutiveCount = 0
            for j in range(B):
                b = random.randint(0,1)
                if b == 0 and b == pb:
                    consecutiveCount +=1
                pb = b
            consecutivecounts.append(consecutiveCount)
        solution = sum(consecutivecounts)/N

        print('simulation solution = ', solution)

    def prg_solve(self):
        solution = 0
        print('programmatic solution = ', solution)

if __name__ == '__main__':
    url = 'https://brilliant.org/daily-problems/two-girls-in-a-row/'
    # define problem inputs
    B = 82 # number of babies
    p = Problem(url, B)
    p.ana_solve()
    p.sim_solve()
    p.prg_solve()


