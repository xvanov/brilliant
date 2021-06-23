import random

class Problem():
    def __init__(self, url, bottom, top):
        self.url = url
        self.bottom = bottom
        self.top = top

    def ana_solve(self):
        solution = 0
        divisible_by_3 = (self.top-self.bottom)/3
        divisible_by_11 = (self.top-self.bottom)/11
        divisible_by_11_and_3 = (self.top-self.bottom)/(11*3)
        divisible = divisible_by_3 + divisible_by_11 - divisible_by_11_and_3
        not_divisible = (self.top-self.bottom) - divisible + 1
        solution = not_divisible
        print('analytical solution = ', solution)

    def sim_solve(self):
        solution = 0
        N_sim = 10000
        freqs = 0
        for n in range(N_sim):
            freqs += self.sim(self.bottom, self.top)
        solution = freqs*(float(self.top)-float(self.bottom))/float(N_sim)
        print('simulation solution = ', solution)

    def sim(self, bottom, top):
        N_reps = 10
        n = 0
        for n in range(N_reps):
            c = random.randint(bottom, top)
            if c % 3 != 0 and c % 11 != 0:
                n += 1
        return n/N_reps

    def prg_solve(self):
        solution = 0
        Z = range(self.bottom, self.top+1)
        for z in Z:
            if z % 3 != 0 and z % 11 != 0:
                solution+=1
        print('programmatic solution = ', solution)

if __name__ == '__main__':
    url = 'https://brilliant.org/daily-problems/not-divisible-3-11/'
    # define problem inputs
    bottom = 1
    top = 100
    p = Problem(url, bottom, top)
    p.ana_solve()
    p.sim_solve()
    p.prg_solve()


