import random

class Problem():
    def __init__(self, url, n_bits, hypothesis):
        self.n_bits = n_bits
        self.hypothesis = hypothesis
        self.url = url
        self.a = self.define_hidden()

    def define_hidden(self):
        a = [random.randint(0,1) for i in range(n_bits)]
        return a

    def bv(self, x, a=None):
        if a == None:
            a = self.a
        N = len(x)
        mul = [a[i]*x[i] for i in range(N)]
        res = sum(mul)%2
        return res

    def hyp(self):
        print(f"hypothesis = {self.hypothesis}")

    def ana_solve(self):
        solution = 0
        print('analytical solution = ', solution)

    def sim_solve(self):
        solution = 0
        print('simulation solution = ', solution)

    def prg_solve(self):
        solution = self.n_bits
        N = 1000
        for j in range(N):
            a = self.define_hidden()
            res = []
            for i in range(solution):
                x = [0]*self.n_bits
                x[i] = 1
                r_tmp = self.bv(x, a)
                res.append(r_tmp)
            print(a)
            print(x)
            print(res)
            assert res == a
        print('programmatic solution = ', solution)

if __name__ == '__main__':
    url = 'https://brilliant.org/practice/finding-the-promise/?p=4'
    # define problem inputs
    n_bits = 4
    hypothesis = f'n_bits = {n_bits}'
    p = Problem(url, n_bits, hypothesis)
    # test
    x = [0,1,1,0]
    r = p.bv(x)
    print(f"a = {p.a}")
    print(f"x = {x}")
    print(f"r = {r}")
    # solve
    p.hyp()
    p.ana_solve()
    p.sim_solve()
    p.prg_solve()


