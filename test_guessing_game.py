import random
import unittest
from guessing_game import GuessingGame


class TestSecret(unittest.TestCase):
    def test_random_secret_always_odd_and_in_range(self):
        for seed in range(500):
            g = GuessingGame(rng=random.Random(seed))
            self.assertEqual(g._secret % 2, 1)
            self.assertTrue(1 <= g._secret <= 1000)


if __name__ == "__main__":
    unittest.main()
