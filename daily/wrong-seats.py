from itertools import permutations
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
        perms = [''.join(p) for p in permutations('ABCDEF')]
        print(perms)
        mask = 'ABCDEF'
        ns = []
        for p in perms:
            tmp = 'ABCDEF'
            tmpns = []
            for i in range(len(mask)):
                tmp = tmp[-1]+tmp[:-1]
                matches = [p[j] == tmp[j] for j in range(len(mask))]
                n_matches = sum(matches)
                tmpns.append(n_matches)
            ns.append(max(tmpns))
        solution = min(ns)

        print('programmatic solution = ', solution)

if __name__ == '__main__':
    url = 'https://brilliant.org/daily-problems/wrong-seats/'
    # define problem inputs
    p = Problem(url)
    p.ana_solve()
    p.sim_solve()
    p.prg_solve()


