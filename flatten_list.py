# 清除嵌套的list

def flat_list(nested_list):
    """把嵌套的list变成一个简单的list"""
    # input your code:
    flated_list = []
    def rec(nested_list):
        for i in nested_list:
            if type(i)==list:
                rec(i)
            else:
                flated_list.append(i)
    recursion(nested_list)
    return flated_list

# 去掉内部rec()的方法
def flat_list(nested_list):
    flattened_list = []
    for i in nested_list:
        if type(i) == list:
            flattened_list += flat_list(i)
        else:
            flattened_list.append(i)
    return flattened_list


if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')

