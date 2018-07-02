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


T = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
print(T) # >>>
# [3, [1], [2, [1], [1]]]

T = tree(1, [tree(5, [tree(7)]), tree(6)])
print(T) # >>>
# [1, [5, [7]], [6]]

# fibonacci tree
def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        return tree(label(left)+label(right), [left, right])

print(fib_tree(4))
# >>>
# [3, [1, [0], [1]], [2, [1], [1, [0], [1]]]]

def count_leaves(t):
    """Count the leaves of a tree"""
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaves(b) for b in branches(t)])

print(count_leaves(fib_tree(4)))
# >>> 5

def leaves(tree):
    """Return a list containing the leaf labels of tree"""
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)], [])

print(leaves(fib_tree(4)))
# >>>
# [0, 1, 1, 0, 1]

def increment_leaves(t):
    """Return a tree like t but with leaf labels incremented"""
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        bs = [increment_leaves(b) for b in branches(t)]
        return tree(label(t), bs)

def increment(t):
    """Return a tree like t but with all labels incremented."""
    return tree(label(t) + 1, [increment(b) for b in branches(t)])


def print_tree(t):
    print(label(t))
    for b in branches(t):
        print_tree(b)

print_tree(fib_tree(4))
# >>>
# 3
# 1
# 0
# 1
# 2
# 1
# 1
# 0
# 1

# new version
def print_tree(t, indent=0):
    print(' ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent+1)

print_tree(fib_tree(4))
# >>>
# 3
#  1
#   0
#   1
#  2
#   1
#   1
#    0
#    1
print_tree(fib_tree(5))
# >>>
# 5
#  2
#   1
#   1
#    0
#    1
#  3
#   1
#    0
#    1
#   2
#    1
#    1
#     0
#     1
