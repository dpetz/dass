""" Example Simulator Parameterization from Appendix A of the DASS paper """

import logic
from scipy import stats


states = {

    'source': '',

    'names': ('bs', 'gs', 'vp', 'vup', 'tpw', 'vw', 'c', 'eos'),

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
        (.01, .07, 0., .03, .34,  0.,  0., .55),  # modified to sum to 1
        (.01, .07, 0., .03, .33,  0., .03, .53),
        (.01, .07, 0., .04, .33,  0., .03, .52),
        (.01, .06, 0., .03, .32, .06,  0., .52),  # modified to sum to 1
        (.01, .06, 0., .03, .32, .06,  0., .52),  # modified to sum to 1
        (.01, .07, 0., .03, .34,  0.,  0., .55),  # modified to sum to 1
        ( 0.,  0., 0.,  0.,  0.,  0.,  0.,  1.)
    )
}
ads = {
    'names': ('sch', 'dsp'),
    'description': ('search', 'display ad'),  # optional
    'states': (('bs',), ('tpw',)),
    'min_impress': (.8, .8),
    'voice_share': (.8, .4),
    'max_freq': (100, 100)
}


def truncnorm(n):
    """Sample user impressibilities from truncated normal distribution. """
    return stats.truncnorm.rvs(0, 1, loc=.8, scale=.1, size=n)


impressibilities = {
    'sch': truncnorm,
    'dsp': truncnorm
}


def verify():
    """Asserts structure of states and ads. """
    logic.states.verify(states)
    logic.ads.verify(ads)
