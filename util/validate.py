
def check_values(data ,predicates):
    """
    If all functions evaluate true when applied to data of same key
    :param data: dictionary of data
    :param predicates: dictionary of functions
    :return:
    """
    return all(predicates[k](data[k]) for k in predicates.keys())

def many(f):
    """Returns function that checks if input contains instances of cls"""
    return lambda iter: all(map(f, iter))


def cls(cls):
    """ Returns function that checks if input is an instance of cls"""
    return lambda obj:  isinstance(obj, cls)


def aligned(iter):
    """If all elements of iter have equal length"""
    return same(len(i) for i in iter)


def approx(x,y, precision=0.00000001):
    """Tests `x == y`` within floating point error tolerance """
    return abs(x - y) < precision


def foreach(iter, f):
    """ Calls ``f`` for all elements of ``iterable``"""
    for obj in iter:
        f(obj)


def iterable(obj):
    """If this is iterable, ie. iter(obj) will work"""
    return hasattr(obj, '__iter__') or hasattr(obj, '__getitem__')
    # @todo: not all requirements checked, see https://www.programiz.com/python-programming/methods/built-in/iter


def same(*objs):
    """ If all are equal. """
    return len(set(objs)) == 1


def counter(n):
    """If n is non-negative int """
    return isinstance(n, int) and (n >= 0)