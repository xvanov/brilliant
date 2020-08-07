class problemMetaInfo():
    def __init__(self):
        self.url = 'https://brilliant.org/daily-problems/table-cloth-pull/'
        self.area = 'Science and Engineering'
        self.featured_course = 'Classic Mechanics'
        self.title = 'Stand, Slide, or Fall'
        self.difficulty = 3 # from 1 to 5
        self.start = '7:41'
        self.end = '8:14'
        self.time = '0:33'
        self.correct = True
class Problem():

    def __init__(self):
        self.mu = 0.5 # coefficient of friction
        self.r = 0.02 # radius [m]
        self.h = 0.05 # height of center of mass [m]
        self.g = -9.8 # [m/s^2]

    def solve(self):
        '''
        Fg = m*g
        Fn = -Fg
        Ff = mu*Fn = -mu*m*g
        Fp = m*a
        Tp = m*a*h
        Tn = -m*g*w
        slide condition: a >= -mu*g
        topple condition: a>= -g*w/h
        '''
        a_slide_min = -self.mu*self.g
        a_topple_min = -self.g*self.r/self.h
        print('Slide min acc = ', a_slide_min)
        print('Topple min acc = ', a_topple_min)
        solution = None
        return solution

if __name__ == '__main__':
    p = Problem()
    solution = p.solve()
    print(f'problem solution: \n{solution}')

