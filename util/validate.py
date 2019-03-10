from functools import partial

def tuple_of(type,obj=None):
    """
    If ``obj`` is provided asserts if its a tuple and its elements are of provided type.
    Otherwise returns a partial functional bound to provided type with single argument obj.
    """
    if obj:
        assert isinstance(obj,tuple)
        assert isinstance(obj[0],type)
        return obj
    else:
        return partial(tuple_of,type)


def approx(x,y, precision=0.00000001):
    """Tests `x == y`` within floating point error tolerance """
    return abs(x - y) < precision


def forall(iterable, f):
    """ Calls ``f`` for all elements of ``iterable``"""
    all(f(obj) for obj in iterable), "'{}' failed for some of: {}".format(f.__name__,iterable)


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