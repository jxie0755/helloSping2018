def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    f1, f2, f3 各为一个函数
    返回一个高阶函数FF, 自带一个参数n,使得FF(n):

    若n == 0, 则return lambda x: x

    若n == 1, 则return lambda x: f1(x)
    若n == 2, 则return lambda x: f2(f1(x))
    若n == 3, 则return lambda x: f3(f2(f1(x))

    若n == 4, 则return lambda x: f1(f3(f2(f1(x))))
    若n == 5, 则return lambda x: f2(f1(f3(f2(f1(x)))))
    若n == 6, 则return lambda x: f3(f2(f1(f3(f2(f1(x))))))

    若n == 7, 则return lambda n: f1(f3(f2(f1(f3(f2(f1(x)))))))
    ...
    ...
    无限叠加
    """


    # 请作答
    pass



if __name__ == '__main__':

    def add1(x):
        return x + 1
    def times2(x):
        return x * 2
    def add3(x):
        return x + 3

    TTest = cycle(add1, times2, add3)

    identity = TTest(0)
    assert identity(0) == 0, 'base test 1'
    assert identity(2) == 2, 'base test 2'

    G =  TTest(2)
    assert G(1) == 4, 'f2(f1(n)), (1+1)*2 = 4'

    H = TTest(3)
    assert H(2) == 9, 'f3(f2(f1(3))), ((2+1)*2)+3 = 9'

    J = TTest(4)
    assert J(2) == 10, 'f1(f3(f2(f1(3)))), (((2+1)*2)+3)+1 = 10'

    K = TTest(6)
    assert K(1) == 19, 'f3(f2(f1(f3(f2(f1(1)))))), (((1+1)*2)+3)+1)*2)+3 = 19'
    
