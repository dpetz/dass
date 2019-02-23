def assert_all_strings(lis):
    return all(isinstance(s, str) for s in lis)

def approx(x,y):
    """Tests x == y within floating point error tolerance """
    return abs(x - y) < 0.00000001

def assert_non_negative(lis):
    assert all(x >= 0 for x in lis), 'Not all elements non-negative: {}'.format(lis)
    return lis

def assert_distribution(lis):
    """Asserts lis contains non_negative numbers that sum to 1."""
    assert_non_negative(lis)
    assert approx(sum(lis),1.0), 'Numbers of probability distribution do not sum to 1.0: {}'.format(sum(lis))
    return lis


def assert_same(*args):
    assert len(set(args)) == 1
    return args