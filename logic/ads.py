"""Ad types. """

from util.validate import *
from util.stats import validate_probability as prob


def verify_ads(data):
    """
    Asserts d is a dict with string keys and iterable values of:
    name -- Unique name of this ad type.
    states -- Set of Activity states on which this ad type can be shown.
    min_impress -- Minimum user impressibility required for the app to be shown (within range [0,1]).
    voice_share -- Probability that ad is actually served to an eligible target user, i.e. a users that meets
                   the minimum ``impressibility`` threshold of the ad type.
    max_freq -- Maximum number of ads that a user can be served of this ad type.

    :return: ads
    """

    validators = {
        'names': seq(cls(str)),
        'states': seq(seq(cls(str))),
        'min_impress': seq(prob),
        'voice_share': seq(prob),
        'max_freq': seq(counter)
    }

    # apply validators to values of data
    verify(values(validators), data)

    verify(aligned, [data[k] for k in validators.keys()])

    return data


def eligible_in_state(ads, state_name):
    """Return indices of ads that can be shown during state"""
    return [i for (i,states) in enumerate(ads['states']) if state_name in states]