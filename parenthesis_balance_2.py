# 请试写一个函数p_balance_recur(str),检测字符串算式的内括号是否平衡
# 只有一种括号形式: ()

# 例:
# p_balance('((()))') == True
# p_balance('()(()') == False
# 注意,算式本身不必合理,只需理会括号之间的逻辑是否合理


# 必须要用递归的方式解决
def p_balance(obj_str,idx=0,tem_list=[]):
    open_bracket =['(','[','{','<']
    close_bracket = [')',']','}','>']
    if idx >= len(obj_str):
        return len(tem_list) == 0
    i = obj_str[idx]
    if i in open_bracket:
        tem_list.append(open_bracket.index(i))
    if i in close_bracket:
            if len(tem_list) == 0:
                return False
            if tem_list.pop() != close_bracket.index(i):
                return False
    return p_balance(obj_str, idx+1, tem_list)
    pass


# Test case:
if __name__ == '__main__':
    assert p_balance('([{}])',0,[]) == True, "example 1"
    assert p_balance('([()}',0,[]) == False, "example 2"
    assert p_balance('((5+3)*2+1)',0,[]) == True, "Simple"
    assert p_balance('{[(3+1)+2]+}',0,[]) == True, "Different types"
    assert p_balance('(3+{1-1)}',0,[]) == False, ",0,[]) is alone inside {}"
    assert p_balance('[1+1]+(2*2)-{3/3}',0,[]) == True, "Different operators"
    assert p_balance('(({[(((1)-2)+3)-3]/3}-3)',0,[]) == False, "the first '(' is redundant"
    assert p_balance('2+3',0,[]) == True, "No brackets, no problem"
    print('all passed')
