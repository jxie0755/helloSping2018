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

# def pingpong(n):
#     """求这个数列的第n项"""
#     def pingpong(idx):
#     a = 1
#     num = 0
#     for i in range(1, idx+1):
#         num += a
#         if i%7 == 0 or is_seven_in(idx):
#             a = -a
#     return num

def pingpong(n):
    def diff(n):
            """Returns the difference between pingpong(n) and pingpong(n-1), which could only be 1 or -1

            这个函数是用递归找两个相邻数字之间的差值,确定是1还是-1
            n为pingpong数列的序号
            这样的话 pingpong(n) = pingpong(n-1) + diff(n)
            """
            if n == 1:
                return 1
            elif (n-1) % 7 == 0 or has_seven(n-1):
                return -1 * diff(n-1)
            else:
                return diff(n-1)
    
    # 这里开始是定义pingpong序列了
    if n == 1:
        return 1  # 起始值为1
    else:
        return pingpong(n-1) + diff(n) # 之后每个数都是上一个数 +1 或者 -1


# def is_seven_in(num):
#     while num > 0:
#         rem = num%10
#         num = num//10
#         if rem == 7:
#             return True
#     return False

# 递归版本is_seven_in
def is_seven_in(num):
    if num % 10 == 7:
        return True
    elif num < 10:
        return False
    else:
        return has_seven(num // 10)



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
