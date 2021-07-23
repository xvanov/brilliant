
class Problem():
    def __init__(self, url, points):
        self.url = url
        self.points = points

    def ana_solve(self):
        solution = 0
        print('analytical solution = ', solution)

    def sim_solve(self):
        solution = 0
        print('simulation solution = ', solution)

    def prg_solve(self):
        solution = []
        N = 20
        lowerbound = -10
        upperbound = 10
        for x in range(lowerbound, upperbound+1):
            for y in range(lowerbound, upperbound+1):
                ptemp = (x, y)
                distance_sum = 0
                for pt in self.points:
                    dtmp = self.manhattan_distance(pt, ptemp)
                    distance_sum += dtmp
                solution.append([ptemp, distance_sum])
        solution.sort(key = lambda x: x[1])
        solution = solution[:10]
        print('programmatic solution = ', solution)

    def manhattan_distance(self, p1, p2):
        x = abs(p1[0] - p2[0])
        y = abs(p1[1] - p2[1])
        d = x+y
        return d

if __name__ == '__main__':
    url = 'https://brilliant.org/daily-problems/taxicab-distance-3/'
    # define problem inputs
    points = [(-3,3), (-3,-4), (2,1)]
    p = Problem(url, points)
    p.ana_solve()
    p.sim_solve()
    p.prg_solve()


