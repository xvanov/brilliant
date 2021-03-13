
class Problem():
    def __init__(self, url):
        self.url = url

    def ana_solve(self):
        solution = 0
        print('analytical solution = ', solution)

    def sim_solve(self):
        solution = 0
        print('simulation solution = ', solution)

    def prg_solve(self):
        solution = 0
        print('programmatic solution = ', solution)

if __name__ == '__main__':
    url = ''
    # define problem inputs
    p = Problem(url)
    p.ana_solve()
    p.sim_solve()
    p.prg_solve()


