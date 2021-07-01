
class Problem():
    def __init__(self, url, point1, point2):
        self.url = url
        self.point1 = point1
        self.point2 = point2

    def ana_solve(self):
        solution = 0
        print('analytical solution = ', solution)

    def sim_solve(self):
        solution = 0
        print('simulation solution = ', solution)

    def prg_solve(self):
        solution = []
        N = 20
        for x in range(20):
            for y in range(20):
                ptemp = (x, y)
                d1 = self.manhattan_distance(self.point1, ptemp)
                d2 = self.manhattan_distance(self.point2, ptemp)
                if d1 == d2:
                    solution.append((ptemp, d1))

        print('programmatic solution = ', solution)

    def manhattan_distance(self, p1, p2):
        x = abs(p1[0] - p2[0])
        y = abs(p1[1] - p2[1])
        d = x+y
        return d
if __name__ == '__main__':
    url = 'https://brilliant.org/daily-problems/taxicab-distance-2/'
    # define problem inputs
    point1 = (4, -2)
    point2 = (-3, 2)
    p = Problem(url, point1, point2)
    p.ana_solve()
    p.sim_solve()
    p.prg_solve()


