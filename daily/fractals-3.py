
class Problem():

    def __init__(self, url):
        self.url = ''

    def solve_sim(self):
        solution = 0
        side = 3/4
        N = 10000
        A = 0
        for i in range(N):
            Atmp = (side**i - side**(i+1))*10*0.5
            A += Atmp

        solution = A
        return solution

    def recur(self, base):
        pass

    def solve_analytic(self):
        result = 1*10*0.5
        return result

if __name__ == '__main__':
    # define problem inputs
    url = 'https://brilliant.org/daily-problems/fractals-3/'

    p = Problem(url)
    solution = p.solve_sim()
    a_sol = p.solve_analytic()
    print(f"simulated solution: {solution}")
    print(f"analytical solution: {a_sol}")
