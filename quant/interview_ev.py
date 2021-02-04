import random
from time import sleep

def ev():
    # number of steps to reach 3 distinct vertices
    p1 = 2/3
    p2 = 1/3
    N = 100
    x = 2
    def recur(x):
        if x > 10:
            return 1
        else:
            return p1*x+p2*recur(x+1)

    p = recur(x)
    print(p)

def sim(N_distinct, vertices, visited):
    current = 0
    steps = 0
    while len(visited) < N_distinct:
        tmp = vertices.copy()
        tmp.remove(current)
        nxt = random.choice(tmp)
        if nxt not in visited:
            visited.append(nxt)
        steps +=1
        #sleep(2)
    return steps

def sim_ev():
    N = 100000
    ss = []
    for i in range(N):
        vertices = [0,1,2,3]
        visited = [0]
        N_distinct = 4
        ss.append(sim(N_distinct, vertices, visited))
    s = sum(ss)/len(ss)
    print(s)

sim_ev()
ev()
