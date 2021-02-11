

if __name__ == '__main__':


    N = 6 # number of beads
    total = 2**N # total combinations
    matched = [] # list of matched binary numbers, so I don't go over them again

    #binary_nums = [format(i, '#08b')[2:] for i in range(0, total)]
    c = 0
    new = []
    for i in range(0, total):
        b = format(i, '#08b')[2:]
        generator_bool = False
        for f in range(2): # flip
            if f == 1:
                b = b[::-1]
            tmp = b
            for j in range(len(b)): # rotate around                
                tmp = tmp[1:]+tmp[0]
                tmp_n = int('0b'+tmp, 2)
                if tmp not in matched:
                    print(i,b,tmp)
                    matched.append(tmp)
                    generator_bool = True

        if generator_bool:
            c+=1
            new.append((i,b))
    print(total)
    print(c)
    print(new)
