# Pingpong数列

# Pingpong数列有这个特征:
# 第一个数为1 (也就是第零项为0)
# 变化只能为 递增1 或者 递减1
# 当遇到第n个数, 如果n这个数字包含7,或者n能被7整除, 则从第n+1项开始反转递增/递减变化

# 数列前30项举例:
# 0 1 2 3 4 5 6 [7] 6 5 4 3 2 1 [0] 1 2 [3] 2 1 0 [-1] 0 1 2 3 4 [5] [4] 5 6
# 0 1            7              14      17         21            27  28    30
# 可以看到 递增/递减 变化规律在遇到第7,14,17,21,27,28后,发生反转

# 特殊规定:
# 代码中不能使用等号!!!!
# 代码中不能使用 "="" !!!!
# 也就是不能使用赋值的命令. 可以使用"=="或者"!="

# 请作答:
def pingpong(n):
    """求这个数列的第n项"""
    pass
    
    

if __name__ == '__main__':
    assert pingpong(7) == 7, '7'
    assert pingpong(8) == 6, '8'
    assert pingpong(15) == 1, '15'
    assert pingpong(22) == 0, '22'
    assert pingpong(30) == 6, '30'
    assert pingpong(68) == 2, '68'
    assert pingpong(69) == 1, '69'
    assert pingpong(70) == 0, '70'
    assert pingpong(71) == 1, '71'
    assert pingpong(72) == 0, '72'
    assert pingpong(100) == 2, '100'
    print('all passed!')
