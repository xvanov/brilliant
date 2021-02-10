import numpy as np

class Series():
    def __init__(self):
        pass

    def geometric_sum(self, b, q):
        '''
        b = first term
        q = common ratio
        '''
        return b/(1-q)

if __name__ == '__main__':
    s = Series()
