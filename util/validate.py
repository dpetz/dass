def string_list(lis):
    assert all(isinstance(s, str) for s in lis)
    return lis

def approx(x,y):
    """Tests x == y within floating point error tolerance """
    return abs(x - y) < 0.00000001

def non_negative_list(lis):
    assert all(x >= 0 for x in lis), 'Not all elements non-negative: {}'.format(lis)
    return lis

def distribution(lis):
    """Asserts lis contains non_negative numbers that sum to 1."""
    non_negative_list(lis)
    assert approx(sum(lis),1.0), 'Numbers of probability distribution do not sum to 1.0: {}'.format(sum(lis))
    return lis

def same(*args):
    assert len(set(args)) == 1
    return args

def probability(x):
    assert type(x) is float
    assert  0 <= x <=  1, 'Probabilities outside range [0,1]: {}'.format(x)
    return x

def counter(n):
    assert type(n) is int
    assert n > 0, 'Not a positive number: {}'.format(n)
    return n