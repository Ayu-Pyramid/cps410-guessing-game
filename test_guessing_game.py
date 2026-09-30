import random
import unittest
from guessing_game import GuessingGame, InvalidGuessError


class TestSecret(unittest.TestCase):
    def test_random_secret_always_odd_and_in_range(self):
        for seed in range(500):
            g = GuessingGame(rng=random.Random(seed))
            self.assertEqual(g._secret % 2, 1)
            self.assertTrue(1 <= g._secret <= 1000)


class TestGuessValidation(unittest.TestCase):
    def setUp(self):
        self.g = GuessingGame(secret=501)

    def test_rejects_even(self):
        with self.assertRaises(InvalidGuessError):
            self.g.guess(500)

    def test_rejects_out_of_range(self):
        for bad in (-1, 0, 1001, 1003):
            with self.assertRaises(InvalidGuessError):
                self.g.guess(bad)

    def test_rejects_non_integers(self):
        for bad in ("5", 3.0, None, True):
            with self.assertRaises(InvalidGuessError):
                self.g.guess(bad)


if __name__ == "__main__":
    unittest.main()
