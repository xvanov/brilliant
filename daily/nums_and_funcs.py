import itertools
import math

class FunctionPermutator():

    def __init__(self):
        pass

    def add(self, num1, num2): return num1+num2
    def mul(self, num1, num2): return num1*num2
    def div(self, num1, num2): return num1/num2
    def sub(self, num1, num2): return num1-num2



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
        allOps = ['+', '-', '*', '/']
        permutedOps = [p for p in itertools.product(allOps, repeat=4)]
        
        results = {}
        for p in permutedOps:
            expression = '2'
            for o in p:
                expression += f'{o}2'
            print(expression, '\n')
            results[expression] = eval(expression)
        results = {k:v for k,v in sorted(results.items(), key=lambda item:item[1])}
        print(results)
        solution = {} 
        for k in results:
            if results[k] == 18:
                solution[k] = 18
        print(len(solution))
        return solution

if __name__ == '__main__':
    p = FunctionPermutator()
    solution = p.solve()
    print(f'problem solution: \n{solution}')

