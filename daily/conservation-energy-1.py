
class Problem():
    def __init__(self, url):
        self.url = url

    def analytical_solve(self):
        solution = 0
        m = 1
        hi = 2
        hf = 2
        vi = 10
        g = 10
        Ei = m*g*hi + 0.5*m*vi**2
        Ef = m*g*hf
        Ekeep = (Ef/Ei)**(1/5)
        Eloss = 1 - Ekeep
        solution = Ekeep
        print(f"Ei = {Ei}")
        print(f"Ef = {Ef}")
        print(f"Ekeep = {Ekeep}")
        print(f"Eloss = {Eloss}")
        return solution


if __name__ == '__main__':
    url = 'https://brilliant.org/daily-problems/conservation-energy-1/'
    # define problem inputs
    p = Problem(url)
    solution = p.analytical_solve()
    print(solution)
