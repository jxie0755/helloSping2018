# 造轮子,写出排列P的函数

# 提示: 
# 使用tree recursion
# enumerate() function might be helpful


def permutations(lst):
    """List all permutations of the given list"""
    pass


    
if __name__ == '__main__':
    assert permutations(['angie', 'cat']) == [['angie', 'cat'], ['cat', 'angie']]
    assert permutations([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    print('all passed')
