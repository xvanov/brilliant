from itertools import combinations
class Problem():
    def __init__(self, url):
        self.url = url

    def solve(self):
        solution = 0
        arr = list(range(1,9))
        c = combinations(arr, 6)
        combos = list(c)
        print(combos)
        print(len(combos))
        worstCase = len(combos)*5
        solution = worstCase
        return solution


if __name__ == '__main__':
    url = 'https://brilliant.org/daily-problems/pigeonhole-2/'
    # define problem inputs
    p = Problem(url)
    solution = p.solve()
    print(solution)
