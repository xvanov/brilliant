

if __name__ == '__main__':
    N = 6 # number of beads
    total = 2**N # total combinations
    matched = [] # list of matched binary numbers, so I don't go over them again

    for i in range(0, total):
        if i not in matched:
            b = format(i, '#08b')[2:]
            print(b[4])
            for f in range(1): # flip
                if f == 1:
                    b = b[::-1]
                tmp = b
                for j in range(len(b)-1): # rotate around                
                    tmp = tmp[1:]+tmp[0]
                    if tmp == b:
                        match = int('0b'+tmp, 2)
                        if match not in matched:
                            #matched.append(match)
                            total -= 1
    print(matched)
    print(total)
