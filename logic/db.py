"""..."""

from tinydb import TinyDB  # , Query
from util.seqs import seq_not_str
import re

tiny = TinyDB('data/tiny.json')


def deep_map(f, obj):
    """Maps elements of a nested data structure recursively.
       For dictionaries f is applied to all values.
       For sequence (as defined by ``util.seqs.seq_not_str``)
       f is applied to all elements."""
    if isinstance(obj, dict):
        return {k: deep_map(f, v) for k, v in obj.items()}
    elif seq_not_str(obj):
        return tuple(deep_map(f, o) for o in obj)
    else:
        return f(obj)


def encode(obj):
    if callable(obj):
        return f'{obj.__module__}.{obj.__qualname__}'
    else:
        return obj


# Python identifier pattern
pid = r'[\w_][\d\w_]'
# Python attribute regex
py_attr = re.compile(f'({pid}+(?:\\.{pid}*)*)(?:\\.)({pid}*)')


def decode(obj):
    """..."""
    if isinstance(obj, str):
        match = re.fullmatch(py_attr, obj)
        if match:
            module = __import__(match.group(1), fromlist=[None])
            func = getattr(module, match.group(2))
            if callable(func):
                return func
    return obj





def search(query):
    """..."""
    return deep_map(decode, tiny.search(query))


def insert(obj):
    """..."""
    tiny.insert(deep_map(encode, obj))