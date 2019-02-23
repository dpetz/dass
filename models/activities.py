from util.assertions import *
import attr
import typing
import numpy as np

@attr.s(frozen=True)
class Stream:
    """ Specifies user browsing behavior in the absence of advertising as first order Markov chain. """

    activity_states = attr.ib(type=typing.List[str])
    """Possible user browsing activities as list of strings,  e.g. ["search", "site visit", "conversion"]"""

    initial_probabilities = attr.ib(convert=assert_distribution)
    """probabilities how users begin browsing stream"""


    def assert_all(self, attribute, value):
        assert_same(
            len(self.activity_states),
            len(self.initial_probabilities),
            value.shape[0],
            value.shape[1]
        )

    transition_matrix = attr.ib(type=np.matrix, validator=assert_all)
    """probabilities of transition from any given activity state to another as [[numpy.matrix]]"""