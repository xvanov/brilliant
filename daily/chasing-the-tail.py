import random
class Problem():
    def __init__(self, url):
        self.url = url

    def ana_solve(self):
        solution = 0
        print('analytical solution = ', solution)

    def sim_solve(self):
        solution = 0
        N = 10000
        allFlips = []
        for i in range(N):
            twoTails = False
            last = random.randint(0,1)
            flips = 1
            while not twoTails:
                current = random.randint(0,1)
                flips +=1
                if last == current and last == 1:
                    twoTails = True
                last = current
            allFlips.append(flips)
        solution = sum(allFlips)/N
        print('simulation solution = ', solution)

    def prg_solve(self):
        solution = 0
        thresh = 0.00001
        current_sum = 99
        running_sum = 0
        n = 2
        while current_sum > thresh:
            current_sum = n/(2.0**n)
            running_sum += current_sum
            n+=1
        solution = running_sum
        print('programmatic solution = ', solution)

if __name__ == '__main__':
    url = 'https://brilliant.org/daily-problems/chasing-the-tail/'
    # define problem inputs
    p = Problem(url)
    p.ana_solve()
    p.sim_solve()
    p.prg_solve()


