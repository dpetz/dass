def all_strings(elems):
    assert all(isinstance(s, str) for s in elems)
    return elems


def approx(x,y, precision=0.00000001):
    """Tests x == y within floating point error tolerance """
    return abs(x - y) < precision


def forall(objs, f):
    all(f(obj) for obj in objs), "'{}' failed for some of: {}".format(f.__name__,objs)


def iterable(obj):
    """Check if this is iterable, ie. iter(obj) will work"""
    return hasattr(obj, '__iter__') or hasattr(obj, '__getitem__')
    # @todo: not all requirements checked, see https://www.programiz.com/python-programming/methods/built-in/iter


def same(*objs):
    """ Assert all element are equal. """
    assert len(set(objs)) == 1
    return objs


def counter(n):
    """Assert n is an int and non-negative"""
    assert type(n) is int
    assert n >= 0, 'Negative counter: {}'.format(n)
    return n


def length(elems,n):
    """Asserts len(elems) == length. Returns n."""
    assert len(elems) == n, '{} entries expected: {}'.format(elems,n)
    return n