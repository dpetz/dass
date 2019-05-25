"""Utility functions for sequences"""


from collections import Sequence
import numpy as np


def join(iterables):
    """Chains and materializes iterable of iterables"""
    from itertools import chain
    return [e for e in chain(*iterables)]


def seq_not_str(obj):
    """If obj is Sequence or np.ndarray but not string."""
    if isinstance(obj, str):
        return False
    return isinstance(obj, Sequence) or isinstance(obj, np.ndarray)


def map_values(dic, f):
    """..."""
    return {k: f(v) for k, v in dic.items()}


# use with https://docs.python.org/3/library/functools.html
def mean(iterable):
    """..."""
    return sum(iterable) / float(len(iterable))


