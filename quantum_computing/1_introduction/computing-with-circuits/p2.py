# common imports
import logging
import sys

# config
logging.getLogger().setLevel(logging.INFO)

# function for adding two numbers together
def add_two_nums(x, y):
    z, c = [], 0
    n = max(len(x), len(y))
    diff_x = n - len(x)
    diff_y = n - len(y)
    if diff_x > 0:
        ins = [0]*diff_x
        x = ins + x
    if diff_y > 0:
        ins = [0]*diff_y
        y = ins + y
    x_r = x[::-1]
    y_r = y[::-1]
    for i in range(n):
        s = x_r[i] + y_r[i] + c
        z.append(s)
        if z[i] >= 10:
            c = 1
            z[i] = z[i] - 10
    if c > 0:
        z.append(c)

    logging.info('adding x and y...')
    logging.info(f'x = {x}')
    logging.info(f'y = {y}')
    logging.info(f'z = {z[::-1]}')


def str_to_list(x):
    l = []
    l[:0] = x
    l =  list(map(lambda n: int(n), l))
    return l


if __name__ == '__main__':
    x = sys.argv[1]
    y = sys.argv[2]
    x = str_to_list(x)
    y = str_to_list(y)
    # logging.info(f'x = {x}')
    # logging.info(f'y = {y}')
    add_two_nums(x, y)

