

if __name__ == '__main__':
    for age in range(10,100):
        ageStr = str(age)
        d1 = int(ageStr[0])
        d2 = int(ageStr[1])
        A = d1*d2*4 + 1
        if A == age:
            print(f'{age} meets criteria')
