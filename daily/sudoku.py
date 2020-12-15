
class Sudoku():
    def __init__(self, alphabet, structure, cols, rows):
        self.alphabet = alphabet
        self.structure = structure
        self.cols = cols
        self.rows = rows

    def check_row(self, row, rowID):
        if sum(row) == self.rows[rowID]:
            return True
        else:
            return False

    def check_column(self, col, colID):
        if sum(col) == self.cols[colID]:
            return True
        else:
            return False

    def iterate_over_possibilites(self):
        # for each column: find all possible combos from alphabet
        # try all permutations of combos for columns and check for 
        # row sum

        pass

    def find_col_combos(self, col):
        pass




if __name__ == '__main__':
    alphabet = [1,1,2,2,2,3,3,4,5,5,5,6]
    structure = [[0,0,99,99,0,0], [0,99,0,0,99,0], [99,0,0,0,0,99]]
    cols = [4,5,6,7,8,9]
    rows = [12,13,14]
    s = Sudoku(alphabet, structure, cols, rows)


