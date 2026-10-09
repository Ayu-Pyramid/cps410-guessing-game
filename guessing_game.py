"""Odd-number guessing game (1-1000). CPS 410 lab.

Architecture:
    GuessingGame  - pure game logic (no I/O), easy to unit test
    play()        - console UI; input/output are injectable for testing
    State         - enum describing where the game is in its lifecycle
"""
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
    """One round of the game: the player guesses a hidden odd integer."""

    MIN, MAX = 1, 1000

    def __init__(self, secret=None, rng=None):
        """Create a round.

        secret: fixed secret (for tests); must be a valid odd number.
        rng:    random source (e.g. random.Random(seed)) for repeatable tests.
        """
        rng = rng or random
        if secret is None:
            # Stepping by 2 from 1 yields only odd numbers: 1, 3, ..., 999.
            secret = rng.randrange(self.MIN, self.MAX + 1, 2)
        self._validate(secret)  # the secret follows the same rules as a guess
        self._secret = secret
        self.attempts = 0
        self.state = State.READY

    @classmethod
    def _validate(cls, value):
        """Raise InvalidGuessError unless value is an odd int in range."""
        # bool is a subclass of int in Python, so reject it explicitly.
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


def play(input_fn=input, output_fn=print, rng=None):
    """Run the console game loop until the player wins or types 'q'.

    Returns the finished GuessingGame, or None if the player quit.
    """
    game = GuessingGame(rng=rng)
    output_fn("Guess the ODD number between 1 and 1000 (q to quit).")
    while game.state is not State.WON:
        text = input_fn("Your guess: ").strip()
        if text.lower() == "q":
            output_fn("Goodbye!")
            return None
        try:
            result = game.guess(int(text))
        except (ValueError, InvalidGuessError) as err:  # non-numeric or rule break
            output_fn(f"Invalid: {err}")
            continue
        output_fn("Correct!" if result == "correct" else f"Too {result.split()[1]}.")
    output_fn(f"You won in {game.attempts} attempts.")
    return game


def main():
    """Play rounds until the player declines a rematch."""
    while True:
        play()
        if input("Play again? (y/n): ").strip().lower() != "y":
            break


if __name__ == "__main__":
    main()
