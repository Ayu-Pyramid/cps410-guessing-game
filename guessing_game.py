import random


class GuessingGame:
    MIN, MAX = 1, 1000

    def __init__(self, rng=None):
        rng = rng or random
        # Stepping by 2 from 1 gives only odd numbers: 1, 3, ..., 999
        self._secret = rng.randrange(self.MIN, self.MAX + 1, 2)
