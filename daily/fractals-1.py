def fractal_area(fractal, diff, side):
    # init
    side = side*fractal
    total = side**2
    diffTmp = total
    i = 1
    # loop
    while diffTmp > diff:
        prev = total
        side = side*fractal
        area = side**2
        total += (2*i)*area
        diffTmp = total-prev
        i+=1
    return total


if __name__ == '__main__':
    fractal = 1/2
    sides = [1, 2**0.5, 2, 2*2**0.5]
    diff = 10**-10
    for s in sides:
        total = fractal_area(fractal,diff,s)
        area = s**2
        print('Side = ', s)
        print('Colored Area = ', total)
        print('Total Area = ', area)
        print('Colored/Total = ', total/area)
        print(' ')

