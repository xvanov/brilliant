from math import sqrt
from itertools import product

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
        functions = ['+', '*', '-', '/']
        possibles = list(product(functions,repeat=3))
        print(possibles)
        results = [11.0,12.0,13.0,14.0]
        print(results)
        for p in possibles:
            operation = f"2.0{p[0]}6.0{p[1]}4.0{p[2]}8.0"
            res = eval(operation)
            if res in results:
                results.remove(res)
                print(operation, res, results)
        print(results)
        solution = results
        print('programmatic solution = ', solution)


if __name__ == '__main__':
    url = 'https://brilliant.org/daily-problems/os-impossible/'
    # define problem inputs
    p = Problem(url)
    p.ana_solve()
    p.sim_solve()
    p.prg_solve()


