""" Statistics utilities """
import random
from util import validate


def validate_probability(x):
    """ Validates x is a float within [0,1]. """
    if not isinstance(x, float):
        return [f'Probability {x} not a float but: {type(x)}']
    if not 0 <= x <= 1:
        return [f'Probability outside range [0,1]: {x}']
    return []


def approx(x, y, precision=0.00001):
    """Tests `x == y`` within precision """
    return abs(x - y) < precision


def validate_pmf(numbers):
    """
    Validates if sequence of numbers are a probability mass function.
    :return n: Empty list is numbers are all non_negative and sum up to 1"""

    msgs = validate.seq(validate_probability)(numbers)

    if not approx(sum(numbers), 1.0):
        msgs.append(f'Probability distribution sums to {sum(numbers)} instead 1.0: {numbers}')

    return msgs


def sample_pmf(pmf,  val=False):
    """Draw index based on probability mass function.
       :param pmf: passes assert_pmf
       :param val: if input to be validated"""

    if val:
        validate.apply(validate_pmf,pmf)

    x = random.random()
    for i, mass in enumerate(pmf):
        if x < mass:
            return i
        x -= mass
    raise ValueError('Not a distribution: {}'.format(pmf))
