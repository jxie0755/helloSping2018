# 完成 class Fib里面的next函数,使得测试能成立

# Fib()起始值默认为0
# next函数能够不断call出下一个斐波那契数

class Fib():
    """A Fibonacci number class"""

    def __init__(self, value=0):
        self.value = value

    def next(self):
        # your code:
        pass

    def __repr__(self):
        return str(self.value)


if __name__ == '__main__':

    start = Fib()
    assert str(start) == '0'
    assert str(start.next().next()) == '1'
    assert str(start.next().next().next()) == '2'
    assert str(start.next().next().next().next()) == '3'
    assert str(start.next().next().next().next().next()) == '5'
    assert str(start.next().next().next().next().next().next()) == '8'
