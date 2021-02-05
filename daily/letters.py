def sum_of_letters(w1, w2, r):
   pass 


def mul_of_letters(w1, w2, r):
    r = 0
    T = 10
    for B in range(T):
        for L in range(T):
            for A in range(T):
                n1 = B*100+L*10+A
                n2 = B*10+A
                r = n1*n2
                tmp = str(r)
                if len(tmp) == 5:
                    Ap = int(tmp[0])
                    Lp = int(tmp[1])
                    A2p = int(tmp[4])
                    if Ap == A2p and Ap == A and Lp == L:
                        print(n1)
                        print(n2)
                        print(r)




if __name__ == '__main__':
