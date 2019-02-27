import numpy as np
from functools import partial

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

def distribution_of_dim(dim):
    return partial(distribution,dim=dim)

def probability(x):
    """ Assert x is a float within [0,1]. """
    assert isinstance(x, float), 'Probability {} not a float but: {}'.format(x,type(x))
    assert  0 <= x <=  1, 'Probability outside range [0,1]: {}'.format(x)
    return x

def distribution(numbers,dim=None):
    """
    Asserts 'numbers' contains non_negative numbers that sum to 1.

    :param numbers: iterable of floats representing probabilities
    :param dim (int or iterable): expected length of numbers  """

    if iterable(dim):
        dim = len(dim)

    if type(dim) is int:
        assert len(numbers) == dim, 'Expected length {}: {}'.format(dim,numbers)

    forall(numbers, probability)

    assert approx(sum(numbers),1.0), 'Numbers of probability distribution do not sum to 1.0: {}'.format(sum(numbers))
    return numbers

def same(*objs):
    """ Assert all element are equal. """
    assert len(set(objs)) == 1
    return objs


def counter(n):
    """Assert n is an int and non-negative"""
    assert type(n) is int
    assert n >= 0, 'Negative counter: {}'.format(n)
    return n

def transition_matrix(mat,n=0):
    assert type(mat) is np.ndarray, 'Not an np.ndarray: {}'.format(type(mat))
    if n:
        assert n == mat.shape[0]
    assert mat.shape[0] == mat.shape[1], '{} rows but {} columns: {}'.format(mat.shape[0], mat.shape[1],mat)
    np.apply_along_axis(distribution,1,mat) # by row

    return mat