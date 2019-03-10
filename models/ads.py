from util import validate, stats
import attr

from util.stats import *

from attr.validators import instance_of


@attr.s(frozen=True)
class Ad:
    name = attr.ib(validator=instance_of(str))
    """" Unique name of this ad type. """

    states = attr.ib(convert=validate.all_strings)
    """ Set of Activity states on which this ad type can be shown. """

    impressibility_threshold = attr.ib(convert=assert_probability)
    """ Minimum user impressibility required for the app to be shown (within range [0,1]). """

    share_of_voice = attr.ib(convert=assert_probability)
    """ Probability that ad is actually served to an eligible target user,
        i.e. a users that meets the minimum ``impressibility`` threshold of the ad type. """

    frequency_cap = attr.ib(convert=validate.counter)
    """ Maximun number of ads that a user can be served of this ad type. """