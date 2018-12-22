# 两个list nums1 和 nums2 都是sorted list
# 但是 nums1 后半部分可能不是, 只不过留出空间给nums2
# 要求是把nums2合并到nums1并保持排序状态
# 只能通过更改nums1, 不能创造任何新的list, 不需要return任何值

# 具体问题请参考test case的例子.

# 另外:
# 改变一个list的方法有lst.pop, lst.insert, lst.remove, 或者直接lst[i] = x.

def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    # your code:


if __name__ == '__main__':
    nums1 = [1]
    nums2 = []
    merge(nums1, 1, nums2, 0)
    assert nums1 == [1], 'Test case 1'

    nums1 = [0]
    nums2 = [1]
    merge(nums1, 0, nums2, 1)
    assert nums1 == [1], 'Test case 2'

    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    merge(nums1, 3, nums2, 3)
    assert nums1 == [1, 2, 2, 3, 5, 6], 'Test case 3'

    nums1 = [1, 5, 7, 0, 0, 0]
    nums2 = [2, 4, 10]
    merge(nums1, 3, nums2, 3)
    assert nums1 == [1, 2, 4, 5, 7, 10], 'Test case 4'

    nums1 = [8, 8, 8, 0, 0, 0]
    nums2 = [1, 2, 3]
    merge(nums1, 3, nums2, 3)
    assert nums1 == [1, 2, 3, 8, 8, 8], 'Test case 5'

    nums1 = [1, 0, 0, 0]
    nums2 = [5, 5, 5]
    merge(nums1, 1, nums2, 3)
    assert nums1 == [1, 5, 5, 5], 'Test case 6'

    nums1 = [1, 2, 4, 5, 6, 0]
    nums2 = [3]
    merge(nums1, 5, nums2, 1)
    assert nums1 == [1, 2, 3, 4, 5, 6], 'Test case 7'

    nums1 = [4, 0, 0, 0, 0, 0]
    nums2 = [1, 2, 3, 5, 6]
    merge(nums1, 1, nums2, 5)
    assert nums1 == [1, 2, 3, 4, 5, 6], 'Test case 8'

    nums1 = [4, 0, 0, 0, 0, 0, 0]
    nums2 = [1, 2, 3, 5, 6]
    merge(nums1, 1, nums2, 5)
    assert nums1 == [1, 2, 3, 4, 5, 6, 0], 'Test case 9'
    
    print('all passed')
    
