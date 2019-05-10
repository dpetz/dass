""" Defines validators or functions that create validators.
A validator is a function that when applied to data returns
a list of detected problems or an empty list otherwise.
The list pattern is used to enable validator composition."""

from util.seqs import seq_not_str, join
from util import stats


prob = stats.validate_probability


def verify(validator, data):
    """Asserts data via validator."""
    result = validator(data)
    assert not result, f'{result}'


def values(validator_dict):
    """ Creates validator applying provided validators to data of same keys
    :param validator_dict: dictionary of functions """

    assert isinstance(validator_dict, dict)

    return lambda data_dict:\
        join(validator_dict[k](data_dict[k]) for k in validator_dict.keys())


def seq(f, n=0):
    """Creates validator applying f to all elements of an iterable (but not a string)."""

    def seq_validator(objs):
        """Function returned"""
        if not seq_not_str(objs):
            return [f'Sequence expected: {objs}']
        if n and n != len(objs):
            return [f'Not of length {n}: {objs}']
        return join(map(f, objs))

    return seq_validator


def cls(typ):
    """ Returns validator if input is an instance of cls."""
    return lambda obj: [] if isinstance(obj, typ) \
        else [f'{obj} not an instance of {typ}']


def aligned(seqs):
    """Validates if all elements of seqs have equal length"""
    return [] if len(set(len(i) for i in seqs)) == 1 else [f'Different lengths: {seqs}']


def same(objs):
    """ If all are equal. """
    return [] if len(set(objs)) == 1 else [f'Not equal: {objs}']


def counter(n):
    """If n is non-negative int """
    return [] if isinstance(n, int) and (n >= 0) else [f'Not a positive integer: {n}']


def size(n):
    """Creates validator if iterable has length n"""
    return lambda seq: [] if len(seq) == n else [f'Length not {n}: {seq}']


def both(left, right):
    """Creates validator collecting results from two other validators."""
    return lambda obj: join((left(obj), right(obj)))