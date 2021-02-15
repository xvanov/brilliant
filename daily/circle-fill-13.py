import sympy as sp
class Problem():
    def __init__(self, url):
        self.url = url
    def solve(self):
        solution = 0
        x = sp.Symbol('x')
        f = x**3+8*x**2-64
        solution = sp.solve(f)
        return solution


if __name__ == '__main__':
   url = 'https://brilliant.org/daily-problems/circle-fill-13/'
   # define problem inputs
   p = Problem(url)
   solution = p.solve()
   print(solution)
