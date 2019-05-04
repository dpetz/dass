"""Utility functions for sequences"""


from collections import Sequence


def join(iterables):
    """Chains and materializes iterable of iterables"""
    from itertools import chain
    return [e for e in chain(*iterables)]


def seq_not_str(obj):
    """If obj is sequence but not string."""
    if isinstance(obj, str):
        return False
    return isinstance(obj, Sequence)
