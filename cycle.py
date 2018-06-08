def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    f1, f2, f3 各为一个函数
    返回一个高阶函数FF, 自带一个参数n,使得FF(n)随着n的变化,成为不同的函数:

    若n == 0, 则 GG = FF(0), 使得GG(x) return x

    若n == 1, 则 GG = FF(1), 使得GG(x) return f1(x)
    若n == 2, 则 GG = FF(2), 使得GG(x) return f2(f1(x))
    若n == 3, 则 GG = FF(3), 使得GG(x) return f3(f2(f1(x))

    若n == 4, 则 GG = FF(4), 使得GG(x) return f1(f3(f2(f1(x))))
    若n == 5, 则 GG = FF(5), 使得GG(x) return f2(f1(f3(f2(f1(x)))))
    若n == 6, 则 GG = FF(6), 使得GG(x) return f3(f2(f1(f3(f2(f1(x))))))

    若n == 7, 则 GG = FF(7), 使得GG(x) return f1(f3(f2(f1(f3(f2(f1(x)))))))
    ...
    ...
    无限叠加
    """


    # 请作答
    
    # 答案:
    def FF(n):
        def g(x):
            i = 0
            while i < n:
                if i % 3 == 0:
                    x = f1(x)
                elif i % 3 == 1:
                    x = f2(x)
                elif i % 3 == 2:
                    x = f3(x)
                i += 1
            return x
        return g
    return FF



if __name__ == '__main__':

    def add1(x):
        return x + 1
    def times2(x):
        return x * 2
    def add3(x):
        return x + 3

    FFtest = cycle(add1, times2, add3)

    GGtest = FFtest(0)
    assert GG(0) == 0, 'base test 1'
    assert GG(2) == 2, 'base test 2'

    GGtest =  FFtest(2)
    assert GGtest(1) == 4, 'f2(f1(n)), (1+1)*2 = 4'

    GGtest = FFtest(3)
    assert GGtest(2) == 9, 'f3(f2(f1(3))), ((2+1)*2)+3 = 9'

    GGtest = FFtest(4)
    assert GGtest(2) == 10, 'f1(f3(f2(f1(3)))), (((2+1)*2)+3)+1 = 10'

    GGtest = FFtest(6)
    assert GGtest(1) == 19, 'f3(f2(f1(f3(f2(f1(1)))))), (((1+1)*2)+3)+1)*2)+3 = 19'
    
    print('all passed')
