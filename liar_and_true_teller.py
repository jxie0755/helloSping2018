# Liars and True Tellers

def truthteller(raw):
    """raw in the form of list"""
    hashtable = {}
    true_statement = 0

    for state in raw[1:]:

        cowA, cowB = state[0], state[2]

        if cowA not in hashtable:
            hashtable[cowA] = 'T'
        elif hashtable[cowA] != 'T':
            break

        if cowB not in hashtable:
            hashtable[cowB] = state[4]
        elif hashtable[cowB] != state[4]:
            break

        true_statement += 1

    return true_statement




if __name__ == '__main__':
    case1 = [
        "4 3",
        "1 4 L", # 1
        "2 3 T", # 2
        "4 1 T", # 3 出现矛盾
    ]  # Example

    # 和上个case开头几乎一样, 但是加一点点
    case2 = [
        "4 6",
        "1 4 L",  # 1
        "2 3 T",  # 2
        "3 1 T",  # 3 改成正确的
        "1 3 T",  # 4 正确
        "3 4 T",  # 5 矛盾
        "3 2 T",  # 6 正确
    ]  # 返回4, 前四条是对的


    assert truthteller(case1) == 2
    assert truthteller(case2) == 4
    print('all passed')
