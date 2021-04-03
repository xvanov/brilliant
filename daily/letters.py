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

def mul_2_digits(w1, w2, r):
    r = 0
    T = 10
    for a in range(T):
        for b in range(T):
            n1 = a*10+b
            n2 = a*10+b
            r = n1*n2
            tmp = str(r)

            # condition
            if len(tmp) >= 4:
                raise Exception(f'result {r} is too big!')
            if len(tmp) < 3:
               continue

            d1 = int(tmp[0])
            d2 = int(tmp[1])
            d3 = int(tmp[2])
            if d2 == a and d3 == b:           
                print(n1,n2,r)
                break
        else:
            continue
        break



if __name__ == '__main__':
    mul_2_digits(0,0,0)
