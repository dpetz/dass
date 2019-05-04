"""Ads"""

from util.validate import *
from util.stats import validate_probability as prob

paper = {
    'names': ('sch', 'dsp'),
    'description': ('search', 'display ad'),  # optional
    'activities': (('bs',), ('tpw',)),
    'min_impress': (.8, .8),
    'voice_share': (.8, .4),
    'max_freq': (100, 100)
}

validators = {
    'names': seq(cls(str)),
    'activities': seq(seq(cls(str))),
    'min_impress': seq(prob),
    'voice_share': seq(prob),
    'max_freq': seq(counter)
}


def validate(data):
    """
    Asserts d is a dict with string keys and iterable values of:
    name -- Unique name of this ad type.
    activities -- Set of Activity states on which this ad type can be shown.
    min_impress -- Minimum user impressibility required for the app to be shown (within range [0,1]).
    voice_share -- Probability that ad is actually served to an eligible target user, i.e. a users that meets
                   the minimum ``impressibility`` threshold of the ad type.
    max_freq -- Maximum number of ads that a user can be served of this ad type.

    :return: ads
    """

    # apply validators to values of data
    apply(values(validators), data)

    apply(aligned, [data[k] for k in validators.keys()])

    return data
