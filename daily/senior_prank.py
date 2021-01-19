

def opposite(i):
    return abs(i-1)

if __name__ == '__main__':
    N = 50
    L = [0]*N
    print(L)
    for i in range(2, N+1):
        for j in range(i,N+1):
            if j%i == 0:
                L[j-1] = opposite(L[j-1])
    print(L)
    i =1
    for l in L:
        print(i, l)
        i+=1
    print(L.count(0), L.count(1))
