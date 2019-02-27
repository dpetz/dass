from util import validate, sample
import attr
from util.sample import Sampler


@attr.s(frozen=True)
class Stream:
    """ Specifies user browsing behavior in the absence of advertising as first order Markov chain. """

    activity_states = attr.ib(convert=validate.all_strings)
    """Possible user browsing activities as list of strings,  e.g. ["search", "organic", "conversion"]"""


    initial_probabilities = attr.ib(convert=validate.distribution)
    """probabilities how users begin browsing stream"""

    # @todo: assert at least one  absorbing state
    # @todo: assert rows and columns are probabilities
    # @todo: assert at least one conversion state and at least two site visit states
    # @todo: assert conversions follow site visit
    # @todo: assert no transitions to ads

    # @todo user specific matrices, e.g. buyers have higher impressability
    # @todo custom rules, e.g. transitions to video watching only from 3rd party website

    transition_matrix = attr.ib(convert=validate.transition_matrix)
    """probabilities of transition from any given activity state to another as [[numpy.matrix]]"""

    def __attrs_post_init__(self):
        validate.same(
            len(self.activity_states),
            len(self.initial_probabilities),
            len(self.transition_matrix)
        )

    def find_absorbing_states(self):
        states = []
        for i, row in enumerate(self.transition_matrix):
            if row[i] == 1.0:
                states.append(i)
        assert len(states) > 0, 'No absorbing state in {}'.format(self.transition_matrix)
        return states


    def simulate(self,n=1,seed=1234):
        sampler = Sampler(seed)
        users=[]
        for user in range(n):
            states = [sampler.draw(self.initial_probabilities)]
            absorbing_states = self.find_absorbing_states()
            while(states[-1] not in absorbing_states):
                states.append(sampler.draw(self.transition_matrix[states[-1]]))
            users.append(states)
        return users