"""
Specifies user browsing behavior in the absence of advertising via a first order Markov chain.
"""

from util.validate import *
from util.stats import *


example = {
    'names': ("Search", "Visit", "Conversion", 'Churn'),
    'initial': (.6, .3, .1, 0.),
    'transitions': ((.3, .5, 0., .2), (.2, .6, .1, .1), (0., 0., 1., 0.), (0., 0., 0., 1.))
}


def absorbing_states(transitions):
    """Checks if activity is absorbing, i.e. `transitions` probabilities to all other activity are zero."""
    return [s for s in range(len(transitions)) if transitions[s][s] == 1.0]


def validate(data):
    """
    Asserts act is a dict with keys:

    `names' -- possible user browsing activities as iterable of strings,  e.g. ['search', 'organic', 'conversion']",
    `initial' -- probabilities how users begin browsing stream as iterable of floats,
    'transitions' -- "probabilities of transition from any given activity state to another as [[numpy.matrix]]"

    :return: `activities`
    """

    n = len(data['names'])
    pmf_n = both(validate_pmf, size(n))

    valid = {
        'names': seq(cls(str)),
        'initial': pmf_n,
        'transitions': seq(pmf_n, n)
    }

    apply(values(valid), data)

    apply(aligned, [data[k] for k in valid.keys()])

    # assert at least on state absorbing
    trans = data['transitions']
    assert len(absorbing_states(trans)) > 0, f'No absorbing state in {trans}'

    return data


paper = {

    'names' : ('bs', 'gs', 'vp', 'vup', 'tpw', 'vw', 'c', 'eos'),

    'descriptions' : (
        'branded search',
        'generic search',
        'visit to a website that the advertiser owns via a click on a paid ad',
        'visit to a website that the advertiser owns via any non-paid click activity',
        'third party website visit (website that does not belong to the advertiser)',
        'video view',
        'conversion',
        'end of session'
    ),

    # all users begin with third party website visit
    'initial': (0., 0., 0., 0., 1., 0., 0., 0.,),

    'transitions': (
        (.01, .07, 0., .05, .33,  0.,  0., .54),
        (.01, .07, 0., .03, .34,  0.,  0., .55),  # modified to add up to 1
        (.01, .07, 0., .03, .33,  0., .03, .53),
        (.01, .07, 0., .04, .33,  0., .03, .52),
        (.01, .06, 0., .03, .32, .06,  0., .52),  # modified to add up to 1
        (.01, .06, 0., .03, .32, .06,  0., .52),  # modified to add up to 1
        (.01, .07, 0., .03, .34,  0.,  0., .55),  # modified to add up to 1
        ( 0.,  0., 0.,  0.,  0.,  0.,  0.,  1.)
    )
}

# @todo: at least two site visit states
# @todo: assert conversions follow site visit
# @todo: assert no transitions to ads
# @todo user specific matrices, e.g. buyers have higher impressibility
# @todo custom rules, e.g. transitions to video watching only from 3rd party website

