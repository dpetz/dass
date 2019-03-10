from attr.validators import instance_of
from util import validate, stats
import attr


@attr.s(frozen=True)
class Activities:
    """ Specifies user browsing behavior in the absence of advertising via a first order Markov chain. """

    names = attr.ib(convert=validate.tuple_of(str))
    """Possible user browsing activities as list of strings,  e.g. ["search", "organic", "conversion"]"""

    initial_probabilities = attr.ib(convert=stats.to_pmf)
    """probabilities how users begin browsing stream"""

    transition_matrix = attr.ib(convert=stats.to_transition_matrix)
    """probabilities of transition from any given activity state to another as [[numpy.matrix]]"""


    def _assert_at_least_one_absorbing(self):
        assert any(self.absorbing(i) for i in range(len(self.names))),\
            'No absorbing state in {}'.format(self.transition_matrix)

    def __attrs_post_init__(self):
        """Called by 'attr' package after attribute initialisation"""
        validate.same(
            len(self.names),
            self.initial_probabilities.size(),
            len(self.transition_matrix)
        )
        self._assert_at_least_one_absorbing()

    def absorbing(self,index):
        """Checks if state is absorbing, i.e. transition_matrix probabilities to all other states are zero."""
        return self.transition_matrix[index][index] == 1.0

    def init(self):
        """Generates first state from initial distribution. """
        return self.initial_probabilities.sample()

    def next(self,state):
        """Generates new states from given state based on transition_matrix."""
        return self.transition_matrix[state].sample()

    @classmethod
    def example(cls):
        return Activities(
            names = ("Search", "Visit" ,"Conversion", 'Churn'),
            initial_probabilities = (.6, .3, .1, 0.),
            transition_matrix = ((.3, .5, 0., .2), (.2, .6, .1, .1), (0., 0., 1., 0.), (0., 0., 0., 1.))
        )

    # @todo: assert at least one conversion state and at least two site visit states
    # @todo: assert conversions follow site visit
    # @todo: assert no transitions to ads
    # @todo user specific matrices, e.g. buyers have higher impressibility
    # @todo custom rules, e.g. transitions to video watching only from 3rd party website


@attr.s(frozen=True)
class Ad:
    name = attr.ib(validator=instance_of(str))
    """" Unique name of this ad type. """

    serving_states = attr.ib(convert=validate.tuple_of(str))
    """ Set of Activity states on which this ad type can be shown. """

    impressibility_threshold = attr.ib(convert=stats.assert_probability)
    """ Minimum user impressibility required for the app to be shown (within range [0,1]). """

    share_of_voice = attr.ib(convert=stats.assert_probability)
    """ Probability that ad is actually served to an eligible target user,
        i.e. a users that meets the minimum ``impressibility`` threshold of the ad type. """

    frequency_cap = attr.ib(convert=validate.counter)
    """ Maximun number of ads that a user can be served of this ad type. """