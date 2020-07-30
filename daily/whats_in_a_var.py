# https://brilliant.org/daily-problems/whats-in-num/
# difficulty = 2
# start = 12:40
# end = 

from itertools import permutations

class numbersGame():
    
    def __init__(self):
        self.mapping = {1:self.subtract, 2:self.add, 3:self.set_to_10, 4:self.square}

    def go_thru(self, permute):
        num = 0
        for  v in permute:
            num = self.num_to_func(v, num)
            print(num)
        return num

    def num_to_func(self, v, num):
        if v == 1:
            return self.subtract(num)
        elif v == 2:
            return self.add(num)
        elif v == 3:
            return self.set_to_10()
        elif v == 4:
            return self.square(num)


    def go_thru_all(self):
        allNums = []
        permutes = list(self.find_all_permutations())
        for p in permutes:
            num = self.go_thru(p)
            allNums.append(num)

        return sorted(allNums), permutes

    def find_all_permutations(self):
        return permutations([1,2,3,4])

    def subtract(self, num):
        return num-5

    def add(self, num):
        return num+5

    def set_to_10(self):
        return 10

    def square(self, num):
        return num*num



if __name__ == '__main__':
    ng = numbersGame()
    allNums, permutes = ng.go_thru_all()
    print(allNums)
    print(permutes)
