# Trees
# A tree contains a root label and a list of branches, each branch is a tree

def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):  # every branch must be a tree as well
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def print_tree(t, indent=0):
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent+1)


# An exampel tree:
TTT = tree(1, [
    tree(2, [
        tree(3, [
            tree(4),
            tree(5)]),
        tree(3, [
            tree(6),
            tree(7)])]),
    tree(2, [
        tree(3, [
            tree(8),
            tree(9)]),
        tree(3, [
            tree(10),
            tree(11)])])])

print_tree(TTT)
# >>>
# 1
#   2
#     3
#       4
#       5
#     3
#       6
#       7
#   2
#     3
#       8
#       9
#     3
#       10
#       11



def tree_max(t):
    """Return the max of a tree."""
    # 找出树内的最大值
    # your code:


def height(t):
    """Return the height of a tree"""
    # 最低层是第几层? 根部为第0层
    # your code:


if __name__ == '__main__':
    assert tree_max(TTT) == 11, 'test tree_max'
    assert height(TTT) == 3, 'test tree height'
    print('all done')
