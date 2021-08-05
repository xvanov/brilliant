from itertools import permutations

class problemMetaInfo():
    def __init__(self):
        self.url = 'https://brilliant.org/daily-problems/variable-order/'
        self.area = 'Science and Engineering'
        self.featured_course = 'Algorithm Fundamentals'
        self.title = 'Don\'t change this variable'
        self.difficulty = 3 # from 1 to 5
        self.start = '5:24'
        self.end = '5:40'
        self.time = '00:16'
        self.correct = True

class Problem():

    def __init__(self):
        pass

    def add_nums(self, num): return num+num
    def add_1(self, num): return num+1
    def mul_3(self, num): return num*3
    def sub_2(self, num): return num-2

    def num_to_func(self, v, num):
        if v == 1:
            return self.add_nums(num)
        elif v == 2:
            return self.add_1(num)
        elif v == 3:
            return self.mul_3(num)
        elif v == 4:
            return self.sub_2(num)

    def go_thru(self, permute):
        num = 0
        for  v in permute:
            num = self.num_to_func(v, num)
            #print(num)
        return num

    def go_thru_all(self):
        allNums = []
        permutes = list(self.find_all_permutations())
        for p in permutes:
            num = self.go_thru(p)
            allNums.append(num)

        return sorted(allNums), permutes

    def find_all_permutations(self):
        return permutations([1,2,3,4])

    def solve(self):
        allNums, permutes = self.go_thru_all()
        print(allNums)
        print(permutes)
        solution = len([1 for n in allNums if n == 0])
        return solution

if __name__ == '__main__':
    p = Problem()
    solution = p.solve()
    print(f'problem solution: \n{solution}')

