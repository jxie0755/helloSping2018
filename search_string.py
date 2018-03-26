def search(target, str_line):
    """return a list of index number of the target in the str_line"""
    
    index_result = []
    index = 0
    length = len(target)
    
    while index <= len(str_line) - length:
        if str_line[index: index + length] == target:
            index_result.append(index)
        index += 1
    
    return index_result
    
sample = 'yeluo123yeluo456yeluo'
print(search('yeluo', sample))
# >>> [0, 8, 16]
