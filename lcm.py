def lcm(X):
    n = 0
    while True:
        n += 1
        for i in range(2,X+1):
            if n%i!=0:
                break
        else:
            break
    return n


def lcm2(X):
    n = 0
    while True:
        n += 1
        if all(n % i == 0 for i in range(2, X+1)):
            return n
