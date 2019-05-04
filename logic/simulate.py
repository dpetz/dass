


from util import stats, validate

def targeted(ad, user):
    """Is user targeted by ad type?"""
    return user.impressibility >= ad.impressibility_threshold




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


