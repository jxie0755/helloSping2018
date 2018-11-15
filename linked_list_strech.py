class Link:
    """A linked list."""
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    @property
    def second(self):
        return self.rest.first

    @second.setter
    def second(self, value):
        self.rest.first = value

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ', '
            self = self.rest
        return string + str(self.first) + '>'


def stretch(s, repeat=0):
    """Replicate the kth element k times, for all k in s."""
    # Your answer #
    pass



if __name__ == '__main__':
    a = Link(3, Link(4, Link(5, Link(6))))
    print(a)
    assert str(a) == '<3, 4, 5, 6>'
    stretch(a)
    assert str(a) == '<3, 4, 4, 5, 5, 5, 6, 6, 6, 6>'
