"""Odd number guessing game (1-1000_.
import random
from enum import Enum

class State(Enum):

  READY = "ready"
  PLAYING = "playing"
  WON = "won"

class InvalidGuessError(ValueError):
 """Raised when a guess is not an odd integer in 1..1000."""

class GuessingGame:
    MIN, MAX = 1, 1000

    def __init__(self, secret=None, rng=None):
        rng = rng or random
        if secret is None:
            secret = rng.randrange(self.MIN, self.MAX + 1, 2)  # odd only
        self._validate(secret)
        self._secret = secret
        self.attempts = 0
        self.state = State.READY

  @classmethod
    def _validate(cls, value):
        if isinstance(value, bool) or not isinstance(value, int):
            raise InvalidGuessError("Guess must be an integer.")
        if not cls.MIN <= value <= cls.MAX:
          raise InvalidGuessError(f"Guess must bee between {cls.MIN} and {cls.MAX}
         if value % 2 == 0:
            raise InvalidGuessError("Guess must be odd.")
def guess(self, value):
        if self.state is State.WON:
            raise RuntimeError("Game is over. Start a new game.")
        self._validate(value)  # invalid guesses don't count as attempts
        self.attempts += 1
        self.state = State.PLAYING
        if value < self._secret:
            return "too low"
        if value > self._secret:
            return "too high"
        self.state = State.WON
        return "correct"
def main():
  game = 
