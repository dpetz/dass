def targeted(ad, user):
    """Is user targeted by ad type?"""
    return user.impressibility >= ad.impressibility_threshold


def streams(states, n=10):
    """Generate n streams based on states"""
    streams = []
    for _ in range(n):
        stream = [states.init()]
        while not states.absorbing(stream[-1]):
            stream.append(states.next(stream[-1]))
        streams.append(stream)
    return streams

#   impressibility = attr.ib(validate.all_probabilites)
#    """probability per ad type that user behavior will change as a result of seeing this ad type.  """
