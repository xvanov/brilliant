from scipy.stats import binom

class Problem():
    def __init__(self, url, N=10, p=0.5, reject=0.03):
        self.url = url
        self.N = N # number of newborns
        self.p = p # probability of being born a boy
        self.reject = reject # rejection criteria for null hypothesis

    def solve(self):
        solution = 0
        print(self.N)
        for k in range(1, self.N):
            prob = binom.pmf(k, self.N, self.p)
            print(k, prob)
            if prob <= self.reject:
                solution = k
        return solution


if __name__ == '__main__':
    url = 'https://brilliant.org/daily-problems/stat-hypothesis-1/'
    # define problem inputs
    N = 10
    p_b = 0.5
    reject = 0.03
    p = Problem(url, N, p_b, reject)
    solution = p.solve()
    print(solution)
