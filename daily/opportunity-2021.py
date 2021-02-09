from itertools import permutations

class Problem():
    def __init__(self, year):
        self.year = year

    def solve(self):
        solution = 0
        yearList = map(int,str(self.year))
        yearPerms = permutations(yearList)
        uniquePerms = set(yearPerms)
        uniqueYears = [u for u in uniquePerms if u[0]!=0]
        print(uniqueYears)
        solution = len(uniqueYears)
        return solution


if __name__ == '__main__':
   year = 2021
   p = Problem(year)
   solution = p.solve()
   print(solution)
