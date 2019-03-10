import attr

from attr.validators import instance_of
from logic.models import Activities, Ad

from util import stats, validate

def targeted(ad, user):
    """Is user targeted by ad type?"""
    return user.impressibility >= ad.impressibility_threshold

class Example:

    names = ('bs', 'gs', 'vp', 'vup', 'tpw', 'vw', 'c', 'eos')

    descriptions = (
        'branded search',
        'generic search',
        'visit to a website that the advertiser owns via a click on a paid ad',
        'visit to a website that the advertiser owns via any non-paid click activity',
        'third party website visit (website that does not belong to the advertiser)',
        'video view',
        'conversion',
        'end of session'
    )

    # all users begin with third party website visit
    initial_probabilities = (0., 0., 0., 0., 1., 0., 0., 0.,)

    transitions = (
        (.01, .07, 0, .05, .33,   0,   0, .54),
        (.01, .07, 0, .03, .34,   0,   0, .54),
        (.01, .07, 0, .03, .33,   0, .03, .53),
        (.01, .07, 0, .04, .33,   0, .03, .52),
        (.01, .06, 0, .03, .32, .06,   0, .51),
        (.01, .06, 0, .03, .32, .06,   0, .51),
        (.01, .07, 0, .03, .34,   0,   0, .54),
        (  0,   0, 0,   0,   0,   0,   0,   1)
    )

    ads = (
        Ad('sch',('bs',),.8,.8,100), #
        Ad('dsp',('tpw',),.8,.4,100) #
    )

    ads_descriptions = ('search', 'display ad')

@attr.s(frozen=True)
class Simulation:

    activities = attr.ib(validator=instance_of(Activities))

    impressibility = attr.ib(convert = stats.to_pmf)
    """probability per ad type that user behavior will change as a result of seeing this ad type.  """

    ads = attr.ib(convert = validate.tuple_of(Ad))

    def streams(self,n=10):
        """Generate n streams based on states"""
        streams = []
        for _ in range(n):
            stream = [self.activities.init()]
            while not self.activities.absorbing(stream[-1]):
                stream.append(self.activities.next(stream[-1]))
            streams.append(stream)
        return streams


