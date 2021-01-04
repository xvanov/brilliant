import random

def random_int_list(R, N):
    randomList = []
    for i in range(N):
        n = random.randint(R[0], R[1])
        randomList.append(n)

    return randomList

def find_ev(R1, R2, N):
    c1 = 0
    list1 = random_int_list(R1,N)
    list2 = random_int_list(R2,N)
    for i in range(N):
        if list1[i] > list2[i]:
            c1 +=1
    return c1/N

if __name__ == "__main__":
    R1 = (1,5)
    R2 = (1,10)
    N = 100000
    val = find_ev(R1, R2, N)
    print(val)
