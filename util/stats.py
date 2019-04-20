import random
from util.validate import *
import attr


def probability(x):
    """ Assert x is a float within [0,1]. """
    if not isinstance(x, float):
        return [f'Probability {x} not a float but: {type(x)}']
    if not 0 <= x <= 1:
        return [f'Probability outside range [0,1]: {x}']
    return []


def pmf(numbers,dim=None):
    """
    Validates 'numbers' contains non_negative numbers summing up to 1. Returns `numbers`.

    :param numbers: iterable of floats representing probabilities
    :param dim (int or iterable): expected length of numbers  """

    if iterable(dim):
        dim = len(dim)

    if type(dim) is int:
        assert len(numbers) == dim, 'Expected length {}: {}'.format(dim,numbers)

    forall(numbers, assert_probability)

    assert approx(sum(numbers),1.0),\
        'Numbers of probability distribution do not sum to 1.0: {}'.format(sum(numbers))
    return True




def transition_matrix(rows,n=0):
    """Validates rows is a valid transition matrix for a Markov process.
       :param rows: iterable (the rows) of iterables (the columns)
       :param n: Expected number of states. 0 (default) if not to be checked. """
    if n:
        length(rows,n)
    else:
        n = len(rows)

    return [assert_pmf(r) for r in rows if length(r,n) ]


def sample_pmf(pmf):
    """Draw single sample from probability mass function.
       :param probabilities: passes assert_pmf"""
    x = random.random()
    for i, mass in enumerate(pmf):
        if x < mass:
            return i
        x -= mass
    raise ValueError('Not a distribution: {}'.format(pmf))
