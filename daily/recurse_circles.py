from math import pi

class Problem():
    def __init__(self, url):
        self.url = url

    def hypothesis(self):
        print('hypothesis = ', 8-2*pi)

    def ana_solve(self):
        solution = 0
        solution = 4*(1-pi/4)*(-1)/(-1/2)
        print('analytical solution = ', solution)

    def sim_solve(self):
        solution = 0
        stop = 0.00001
        def recurse(s):
            A = self._get_area(s)
            if A < stop:
                return 0
            else:
                new_s = self._get_side(s)
                return A + recurse(new_s)
        s = 2
        solution = recurse(s)
        print('simulation solution = ', solution)

    def prg_solve(self):
        solution = 0
        N = 1000
        s = 2
        A = 0
        for i in range(N):
            A += self._get_area(s)
            s = self._get_side(s)
        solution = A
        print('programmatic solution = ', solution)

    def _get_area(self, s):
        return s**2 - (pi*s**2)/4

    def _get_side(self, s):
        return 2**(1/2)/2*s

if __name__ == '__main__':
    url = 'https://brilliant.org/daily-problems/fractals-2/'
    # define problem inputs
    p = Problem(url)
    p.hypothesis()
    p.ana_solve()
    p.sim_solve()
    p.prg_solve()

