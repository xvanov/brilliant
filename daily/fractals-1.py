
class Problem():

    def __init__(self, url):
        self.url = ''

    def solve_sim(self):
        solution = 0
        side = 2**0.5
        solution = self.recur(side)
        return solution

    def recur(self, side):
        if side < 0.0001:
            return 0
        else:
            return (side/2)**2 + 2*self.recur(side/2)

    def solve_analytic(self):
        pass

if __name__ == '__main__':
    # define problem inputs
    url = 'https://brilliant.org/daily-problems/fractals-1/'

    p = Problem(url)
    solution = p.solve_sim()
    print(solution)
