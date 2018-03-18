def lcm(X):
    n = 0
    while True:
        n += 1
        for i in range(2,X+1):
            if n % i != 0:
                break
        else:
            break  #　太多break
    return n


# 至少应该是
def lcm_b(X):
    n = 0
    while True:
        n += 1
        for i in range(2,X+1):
            if n % i != 0:
                break
        else:
            return n     # 直接return n

        

def lcm2(X):
    n = 0
    while True:
        n += 1
        if all(n % i == 0 for i in range(2, X+1)):  # 或者是用all()来判断,只有整个遍历所有i都能整除,才为True
            return n


