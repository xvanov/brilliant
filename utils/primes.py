

def is_prime(n):
    prime = True
    if n > 1:
        for i in range(2, n):
            if (n%i) == 0:
                prime = False
                break
    else:
        prime = False
    return prime

if __name__ == '__main__':
    for n in range(100):
        if is_prime(n):
            print(n)
