class problemMetaInfo():
    def __init__(self):
        self.url = ''
        self.area = ''
        self.title = ''
        self.difficulty = 1 # from 1 to 5
        self.start = '10:30'
        self.end = '12:20'
        self.time = '01:50'

class Problem():

    def __init__(self):
        pass

    def solve(self):
        solution = None
        return solution

if __name__ == '__main__':
    p = Problem()
    solution = p.solve()
    print(f'problem solution: \n{solution}')

