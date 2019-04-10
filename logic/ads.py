from util.validate import *
from util.stats import *


paper = {
    'names' : ('sch','dsp'),
    'description' : ('search', 'display ad'),  # optional
    'activities' : (('bs',), ('tpw',)),
    'min_impress' : (.8, .8),
    'voice_share' : (.8, .4),
    'max_freq': (100, 100)
}


def validate(ads):
    """
    Asserts d is a dict with string keys:
    name -- Unique name of this ad type.
    activities -- Set of Activity states on which this ad type can be shown.
    min_impress -- Minimum user impressibility required for the app to be shown (within range [0,1]).
    voice_share -- Probability that ad is actually served to an eligible target user, i.e. a users that meets the minimum ``impressibility`` threshold of the ad type.
    max_freq -- Maximum number of ads that a user can be served of this ad type.

    :return: ads
    """

    signatures = {
        'names': many(cls(str)),
        'activities': many(many(cls(str))),
        'min_impress': many(probability),
        'voice_share': many(probability),
        'max_freq': many((counter))
    }

    assert check_values(ads, signatures)

    assert aligned(ads.values())

    return ads
