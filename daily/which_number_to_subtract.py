url = 'https://brilliant.org/daily-problems/subtract-square-nim/'
area = 'Math and Logic'
title = 'Which Square to Subtract?'
diffulty = 5
start = '10:30'
end = '12:20'
time = '01:50'



class SquareNumberGame():

    def __init__(self, N):
        self.N = N
        self.squares = self.squares(N)

    def go_thru(self):
        current = self.N
        squares = self.squares
        parity = True

        def recurse(current, squares, parity):
            newPosses = [current-s for s in squares if s <= current]
            victories = []
            for possibility in newPosses:
                if possibility == 0:
                    victories.append((0, parity, -1))
                else:
                    listOfVictories = recurse(possibility, squares, not parity)
                    for lv in listOfVictories:
                        lowerParity = lv[1]
                    victories.append((possibility,lowerParity,listOfVictories))
            return victories

        listOfLists = recurse(current, squares, parity)
        self.recursionTree = listOfLists
        #print(listOfLists)

    def parse_tree(self):
        for branch in self.recursionTree:
            print(branch[0], branch[1])

    def squares(self, N):
        num = 1
        squares = []
        while num**2 <= N:
            squares.append(num**2)
            num += 1
        return squares


if __name__ == '__main__':
    N = 9
    sng = SquareNumberGame(N)
    print(f'beginning game...\n N = {N}\n squares less than N = {sng.squares}')
    sng.go_thru()
    sng.parse_tree()


