
class RandomGenerator:
    """
    Uses Blum Blum Shub: https://en.wikipedia.org/wiki/Blum_Blum_Shub
    Primes are randomly generated by https://asecuritysite.com/encryption/random3?val=32
    This very much does not need to be secure, but I thought I'd use a simple one
    """
    def __init__(self, seed, m=2885585089 * 2485699771):
        self._state = seed % (m - 2) + 2
        self.m = m
        while self._state ** 2 < self.m:
            self._step()

    def _step(self):
        self._state = self._state ** 2 % self.m

    def rand(self, maximum):
        """
        Generate a random number in the range [0, maximum)
        """
        assert maximum * maximum < self.m
        self._step()
        return self._state % maximum

    def choose(self, lst):
        """
        Choose a random element of the list lst
        """
        return lst[self.rand(len(lst))]
