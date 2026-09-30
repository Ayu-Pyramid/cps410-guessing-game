import random
from enum import Enum


class State(Enum):
    """Lifecycle of one game round."""
    READY = "ready"      # no valid guess made yet
    PLAYING = "playing"  # at least one wrong guess made
    WON = "won"          # secret found; round is over


class InvalidGuessError(ValueError):
    """Raised when a guess is not an odd integer in 1..1000."""


class GuessingGame:
    MIN, MAX = 1, 1000

    def __init__(self, secret=None, rng=None):
        rng = rng or random
        if secret is None:
            # Stepping by 2 from 1 gives only odd numbers: 1, 3, ..., 999
            secret = rng.randrange(self.MIN, self.MAX + 1, 2)
        self._secret = secret
        self.attempts = 0
        self.state = State.READY

    @classmethod
    def _validate(cls, value):
        # bool is a subclass of int in Python, so reject it explicitly
        if isinstance(value, bool) or not isinstance(value, int):
            raise InvalidGuessError("Guess must be an integer.")
        if not cls.MIN <= value <= cls.MAX:
            raise InvalidGuessError(f"Guess must be between {cls.MIN} and {cls.MAX}.")
        if value % 2 == 0:
            raise InvalidGuessError("Guess must be odd.")

    def guess(self, value):
        """Check a guess; return 'too low', 'too high' or 'correct'."""
        if self.state is State.WON:
            raise RuntimeError("Game is over. Start a new game.")
        self._validate(value)  # invalid guesses are not counted as attempts
        self.attempts += 1
        self.state = State.PLAYING
        if value < self._secret:
            return "too low"
        if value > self._secret:
            return "too high"
        self.state = State.WON
        return "correct"
