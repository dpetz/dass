import random
# from functools import partial
from util.validate import *
import attr


def assert_distribution_of_dim(dim):
    return partial(assert_distribution,dim=dim)


def assert_probability(x):
    """ Assert x is a float within [0,1]. """
    assert isinstance(x, float), 'Probability {} not a float but: {}'.format(x,type(x))
    assert 0 <= x <= 1, 'Probability outside range [0,1]: {}'.format(x)
    return x


def assert_distribution(numbers,dim=None):
    """
    Asserts 'numbers' contains non_negative numbers that sum to 1.

    :param numbers: iterable of floats representing probabilities
    :param dim (int or iterable): expected length of numbers  """

    if iterable(dim):
        dim = len(dim)

    if type(dim) is int:
        assert len(numbers) == dim, 'Expected length {}: {}'.format(dim,numbers)

    forall(numbers, assert_probability)

    assert approx(sum(numbers),1.0),\
        'Numbers of probability distribution do not sum to 1.0: {}'.format(sum(numbers))
    return numbers


def to_pmf(probabilities):
    return PMF(probabilities)


def to_transition_matrix(rows,n=0):
    """Assert rows is a valid transition matrix for a Markov process.

       :param n: Expected number of states. 0 (default) if not to be checked. """
    if n:
        length(rows,n)
    else:
        n = len(rows)

    return [to_pmf(r) for r in rows if length(r,n) ]


@attr.s(frozen=True)
class PMF:

    probabilities = attr.ib(convert=assert_distribution)
    """List of probabilities"""

    def size(self):
        return len(self.probabilities)

    def __getitem__(self,index):
        return self.probabilities[index]

    def sample(self):
        """Draw single sample from probability mass function."""
        x = random.random()
        for i, mass in enumerate(self.probabilities):
            if x < mass:
                return i
            x -= mass
        raise ValueError('Not a distribution: {}'.format(self.probabilities))