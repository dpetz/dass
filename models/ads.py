from util import validate
import attr
import typing

from attr.validators import instance_of

@attr.s(frozen=True)
class Ads:
    ad_types = attr.ib(type=typing.List[str])
    """Possible user browsing activities as list of strings,  e.g. ["search", "display", "video"]"""


@attr.s(frozen=True)
class AdType:
    name = attr.ib(validator=instance_of(str))
    """" Unique name of this ad type"""

    states = attr.ib(convert=validate.string_list)
    """ Set of Activity states on which this ad type can be shown. """

    impressibility = attr.ib(convert=validate.probability)
    """ Miminum user impressibility treshold for the app to be shown (within range [0,1]) """

    share_of_voice = attr.ib(convert=validate.probability)
    """ Probability that ad is actually served to an eligible target user,
        i.e. a users that meets the minimum ``impressibility`` treshold of the ad type"""

    frequency_cap = attr.ib(validator=instance_of(int),convert=validate.counter)
    """Maximun number of ads that a user can be served of this ad type. """