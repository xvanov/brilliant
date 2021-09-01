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
        solution = 0
        functions = ['+', '*', '-', '/']
        possibles = list(product(functions,repeat=3))
        print(possibles)
        primes = []
        for p in possibles:
            res = eval(f"5.0{p[0]}5.0{p[1]}5.0{p[2]}5.0")
            print(res)
            is_prime = self.is_prime(res)
            if is_prime:
                primes.append((p, res))
        print(f'primes = {primes}')
        soution = len(primes)
        print('programmatic solution = ', solution)

    def is_prime(self, n):
        prime_flag = True
        if n > 1 and n.is_integer():
            for i in range(2, int(sqrt(n)) + 1):
                if (n % i == 0):
                    prime_flag = False
                    break
        else :
            prime_flag = False
        return prime_flag

if __name__ == '__main__':
    url = 'https://brilliant.org/daily-problems/os-prime-5/'
    # define problem inputs
    p = Problem(url)
    p.ana_solve()
    p.sim_solve()
    p.prg_solve()


