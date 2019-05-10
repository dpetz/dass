"""
Specifies user browsing behavior in the absence of advertising via a first order Markov chain.
States (also called activities in the paper) are represented by dictionaries that pass ``verify``.
"""

from util.validate import *
from util.stats import *


example = {
    'names': ("Search", "Visit", "Conversion", 'Churn'),
    'initial': (.6, .3, .1, 0.),
    'transitions': ((.3, .5, 0., .2), (.2, .6, .1, .1), (0., 0., 1., 0.), (0., 0., 0., 1.))
}


def absorbing(state):
    """Return indices of absorbing states, i.e. `transitions` probabilities to all other activity are zero."""
    trans = state['transitions']
    return [s for s in range(len(trans)) if trans[s][s] == 1.0]


def init(state):
    """ Sample initial/first activity. """
    return sample_pmf(state['initial'])


def progress(state, act):
    """Transition to next activity / state. """
    return sample_pmf(act['transitions'][state])


def verify_states(states):
    """
    Asserts act is a dict with keys:

    `names' -- possible user browsing activities as iterable of strings,  e.g. ['search', 'organic', 'conversion']",
    `initial' -- probabilities how users begin browsing stream as iterable of floats,
    'transitions' -- "probabilities of transition from any given activity state to another as [[numpy.matrix]]"

    :return: `activities`
    """

    n = len(states['names'])
    pmf_n = both(validate_pmf, size(n))

    spec = {
        'names': seq(cls(str)),
        'initial': pmf_n,
        'transitions': seq(pmf_n, n)
    }

    verify(values(spec), states)

    verify(aligned, [states[k] for k in spec.keys()])

    # assert at least on state absorbing
    assert len(absorbing(states)) > 0, f"No absorbing state in {states['transitions']}"

    return states

# @todo: at least two site visit states
# @todo: assert conversions follow site visit
# @todo: assert no transitions to ads
# @todo user specific matrices, e.g. buyers have higher impressibility
# @todo custom rules, e.g. transitions to video watching only from 3rd party website

