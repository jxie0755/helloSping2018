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
    
def premutation(num):
    length = num
    total_idx = pow(num,num)
    count = 0
    total_prem = []
    for idx in range(0,total_idx):
        N = idx
        tem_list = []
        for p in range(0, length):
            addition = int(N/pow(length,p))%length+1
            if addition not in tem_list:
                tem_list.append(addition)
        if len(tem_list) == length:
            count += 1
            total_prem.append(tem_list)
    return total_prem

def premutate_a_list(lst):
    pass

test_prem = premutation

print(test_prem(3))

    
    
    
    
    
    
    
    
    
    
 
    # 答案
def permutations(lst):
    """List all permutations of the given list"""
    ### Your code here ###
    if len(lst) <= 1:
        return [lst]
    total = []
    for i, k in enumerate(lst):
        total.extend([[k] + p for p in permutations(lst[:i] + lst[i+1:])])
    return total
