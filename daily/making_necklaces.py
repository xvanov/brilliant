

if __name__ == '__main__':


    N = 6 # number of beads
    total = 2**N # total combinations
    matched = [] # list of matched binary numbers, so I don't go over them again

    binary_nums = [format(i, '#08b')[2:] for i in range(0, total)]
    


    for i in range(0, total):
        if i not in matched:
            b = format(i, '#08b')[2:]
            for f in range(1): # flip
                if f == 1:
                    b = b[::-1]
                tmp = b
                for j in range(len(b)): # rotate around                
                    tmp = tmp[1:]+tmp[0]
                    tmp_b = int('0b'+tmp, 2)
                    if tmp_b not in matched:
                        matched.append(tmp_b)
        else:
            print(i)
            matched.append(i)
    unique_matched = set(matched)
    print(matched)
    print(len(unique_matched))
