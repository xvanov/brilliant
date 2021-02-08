import random

'''
5\cdot5\cdot\frac{4}{11^{2}\cdot10}+5\cdot5\cdot\frac{4}{11^{2}\cdot10}

'''
def run_sim(y, b, r, N):
    wins = [pick_marbles(y,b,r) for n in range(N)]
    return sum(wins)/len(wins)

def pick_marbles(y,b,r):
    ys = [0]*y
    bs = [1]*b
    rs = [2]*r

    t = ys+bs+rs
    st = random.choice(t)
    picks = random.sample(t,2)
    picks.append(st)
    if picks[0] == picks[1] and picks[1] == picks[2]:
        win = True
    else:
        win = False
    return win

if __name__ == '__main__':
    Y = 1
    B = 5
    R = range(4,8)
    N = 100000

    res = [run_sim(Y, B, r, N) for r in R]
    print(res)
