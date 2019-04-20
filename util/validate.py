""" Defines validators or functions that create validators.
A validator is a function that when applied to data returns
a list either containing detected problems or empty otherwise. """


from collections import Sequence


def apply_assert(validator, data):
    """Asserts data via validator."""
    result = validator(data)
    assert not result, f'{result}'


def seq_not_str(obj):
    """If obj is sequence but not string."""
    if isinstance(obj, str):
        return False
    return isinstance(obj, Sequence)


def join(lists):
    """Chains and materializes lists"""
    from itertools import chain
    return [e for e in chain(*lists)]


def values(validator_dict):
    """
    Collects messages from all validators when applied to data of same key
    :param data_dict: dictionary of data
    :param validator_dict: dictionary of functions
    :return:
    """
    return lambda data_dict:\
        join(validator_dict[k](data_dict[k]) for k in validator_dict.keys())


def seq(f):
    """Returns function that evaluates f to all elements of an iterable and returns list of messages """

    return lambda seq: join(map(f, seq)) \
        if seq_not_str(seq) else [f'Sequence (except strings) expected: {seq}']


def cls(cls):
    """ Validates if input is an instance of cls."""
    return lambda obj: [] if isinstance(obj, cls) \
        else [f'{obj} not an instance of {cls}']


def aligned(seq):
    """If all elements of iter have equal length"""
    return [] if len(set(len(i) for i in seq)) == 1 else [f'Different lengths: {seq}']


def approx(x,y, precision=0.00000001):
    """Tests `x == y`` within floating point error tolerance """
    return abs(x - y) < precision


def same(objs):
    """ If all are equal. """
    return [] if len(set(objs)) == 1 else [f'Not equal: {objs}']


def counter(n):
    """If n is non-negative int """
    return [] if isinstance(n, int) and (n >= 0) else [f'Not a positive integer: {n}']