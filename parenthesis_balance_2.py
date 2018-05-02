# 请试写一个函数p_balance_recur(str),检测字符串算式的内括号是否平衡
# 只有一种括号形式: ()

# 例:
# p_balance('((()))') == True
# p_balance('()(()') == False
# 注意,算式本身不必合理,只需理会括号之间的逻辑是否合理


# 必须要用递归的方式解决
def p_balance_recur(tem_str):
    pass


# Test case:
if __name__ == '__main__':
    assert p_balance('((()))') == True, "example 1"
    assert p_balance('()(()') == False, "example 2"
    assert p_balance('((5+3)*2+1)') == True, "Simple"
    assert p_balance(')9+9(') == True, "Opposite direction"
    assert p_balance('(abcd(') == False, "same direction"
    assert p_balance('(1+1)+(2*2)-(3/3)') == True, "Different operators"
    assert p_balance('(1(()+)2)a)bcd()') == False, "additional"
    assert p_balance('2+3') == True, "No brackets, no problem"
    print('all passed')
