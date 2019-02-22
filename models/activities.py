from util.assertions import *

#@attr.s(frozen=True, auto_attribs = True)
class Stream:
    """ Specifies user browsing behavior in the absence of advertising as first order Markov chain. """

    def __init__(self,activity_states, initial_probabilities, transition_matrix):
        """
        :param activity_states: possible user browsing activities as list of strings,
                                e.g. ["search", "site visit", "conversion"].
        :param initial_probabilities: probabilities how users begin browsing stream
        :param transition_matrix: probabilities of transition from any given activity state to another as [[numpy.matrix]]

        """
        assert_all_strings(activity_states)
        assert_distribution(initial_probabilities)
        assert len(activity_states) == len(initial_probabilities)

        self.activity_states = activity_states
        self.initial_probabilities = initial_probabilities
        self.transition_matrix = transition_matrix

    def __str__(self):
         return '{} transformed by {}'.format(
            list(zip(self.activity_states,self.initial_probabilities)),
            self.transition_matrix
        )
