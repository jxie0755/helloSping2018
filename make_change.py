# 手上有3种币值 (其中一个必定是1块,另外两个不确定)
# 请计算最少需要几张货币完成找钱

# 举例说明:
# 手上有 1, 3, 4 三种币值,
# 那么找5块钱就是: 1 + 4 = 5 -- 2张
# 那么找6块钱就是: 3 + 3 = 6 ---2张, 注意不是 1+1+4 = 6 -- 3张
# 如果是12块钱就是: 4+4+4 = 12 -- 3张, 注意不是 3+3+3+3 = 12 --- 4张

def make_change(n, a, b):
    """n为需要找的钱, ab分别为两个面值, 且1<a<b
    需要返回最少找几张钱

    注意: 手上必有1块的面值, 为确保能找得开
    """
    # your code:


if __name__ == '__main__':
    assert make_change(5, 3, 4) == 2, 'Example 1'
    assert make_change(6, 3, 4) == 2, 'Example 2'
    assert make_change(9, 3, 4) == 3, '3+3+3'
    assert make_change(11, 3, 4) == 3, '4+4+3'
    assert make_change(12, 3, 4) == 3, 'Example 3'
    assert make_change(30, 3, 4) == 8, '4*6 + 1 + 1'
    assert make_change(7, 3, 5) == 3, '3+3+1 or 5+1+1, both work'
    assert make_change(49, 7, 9) == 7, '7*7'
    assert make_change(27, 5, 8) == 5, 'not 8*3+1*3, not 5*5+1*2, but 5*4 + 8*1'
    print('All passed')
