import random

class Sampler:

    def __init__(self,seed=1234):
        self.rand = random.Random(seed)

    def draw(self,pmf):
        """:param pmf: probability mass functions """
        x = self.rand.random()
        for i, mass in enumerate(pmf):
            if x < mass:
                return i
            x -= mass
        raise ValueError('Not a distribution: {}'.format(pmf))

