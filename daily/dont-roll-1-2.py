import random

class Problem():
    def __init__(self, url):
        self.url = url

    def ana_solve(self):
        solution = 0
        # d = 1/3*3/2 + 2/3*(9/2 + d)
        d = 3*(1/3*3/2 + 2/3*9/2)
        solution = d
        print('analytical solution = ', solution)

    def sim_solve(self):
        solution = 0
        N = 10000
        totals = []
        for i in range(N):
            quit = False
            total = 0
            while not quit:
                roll = random.randint(1,6)
                total += roll
                if roll == 1 or roll == 2:
                    quit = True
            totals.append(total)

        solution = sum(totals)/N

        print('simulation solution = ', solution)

    def prg_solve(self):
        solution = 0
        N = 100
        tmp_sum = 0
        for i in range(100):
            tmp_sum += self.serie(i)
        solution = tmp_sum
        print('programmatic solution = ', solution)

    def serie(self, i):
        value = (1/6)**(i+1)*(3*4**i + 18*i*2**(2*i-1))
        return value


if __name__ == '__main__':
    url = 'https://brilliant.org/daily-problems/dont-roll-1-2/'
    # define problem inputs
    p = Problem(url)
    p.ana_solve()
    p.sim_solve()
    p.prg_solve()


