from util import validate
import attr

@attr.s(frozen=True)
class Stream:
    """ Specifies user browsing behavior in the absence of advertising as first order Markov chain. """

    activity_states = attr.ib(convert=validate.string_list)
    """Possible user browsing activities as list of strings,  e.g. ["search", "organic", "conversion"]"""

    initial_probabilities = attr.ib(convert=validate.distribution)
    """probabilities how users begin browsing stream"""


    def assert_transitions(self, _, matrix):

        # all objects sized for same number of activities
        validate.same(
            len(self.activity_states),
            len(self.initial_probabilities),
            matrix.shape[0],
            matrix.shape[1]
        )
        # @todo: assert at least one  absorbing state
        # @todo: assert rows and columns are probabilities
        # @todo: assert at least one conversion state and at least two site visit states
        # @todo: assert conversions follow site visit
        # @todo: assert no transitions to ads

        # @todo user specific matrices, e.g. buyers have higher impressability
        # @todo custom rules, e.g. transitions to video watching only from 3rd party website

    transition_matrix = attr.ib(validator=assert_transitions)
    """probabilities of transition from any given activity state to another as [[numpy.matrix]]"""