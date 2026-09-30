import random
import unittest
from guessing_game import GuessingGame, InvalidGuessError, State


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


class TestGuessResults(unittest.TestCase):
    def setUp(self):
        self.g = GuessingGame(secret=501)

    def test_too_low(self):
        self.assertEqual(self.g.guess(101), "too low")

    def test_too_high(self):
        self.assertEqual(self.g.guess(999), "too high")

    def test_correct(self):
        self.assertEqual(self.g.guess(501), "correct")


class TestStateAndAttempts(unittest.TestCase):
    def test_initial_state(self):
        g = GuessingGame(secret=7)
        self.assertEqual((g.state, g.attempts), (State.READY, 0))

    def test_playing_after_wrong_guess(self):
        g = GuessingGame(secret=7)
        g.guess(1)
        self.assertEqual(g.state, State.PLAYING)

    def test_won_after_correct_guess(self):
        g = GuessingGame(secret=7)
        g.guess(7)
        self.assertEqual(g.state, State.WON)

    def test_invalid_guess_not_counted(self):
        g = GuessingGame(secret=7)
        with self.assertRaises(InvalidGuessError):
            g.guess(4)
        self.assertEqual(g.attempts, 0)

    def test_attempts_counted(self):
        g = GuessingGame(secret=7)
        g.guess(1)
        g.guess(9)
        g.guess(7)
        self.assertEqual(g.attempts, 3)

    def test_no_guess_after_win(self):
        g = GuessingGame(secret=7)
        g.guess(7)
        with self.assertRaises(RuntimeError):
            g.guess(7)


if __name__ == "__main__":
    unittest.main()
