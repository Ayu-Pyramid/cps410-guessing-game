# CPS 410 Guessing Game

## Overview

The CPS 410 Guessing Game is a Python command-line game where players try to guess a randomly generated odd integer between 1 and 1000. The game provides feedback after each valid guess, indicating whether the guess is too high, too low, or correct.

Players can quit at any time or choose to play another round after finishing a game.

## Game Rules

- The secret number is an odd integer between 1 and 999.
- Guesses must be integers between 1 and 1000.
- Even numbers, non-integer values, and out-of-range guesses are rejected.
- Invalid guesses do not count toward the attempt total.
- The game tracks the number of valid guesses and ends when the secret number is found.
- Players can enter `q` to quit the current round.

## Program Structure

### `guessing_game.py`

The main program contains the game logic and console interface.

- **`State`**: An enumeration representing the game's three states: `READY`, `PLAYING`, and `WON`.
- **`InvalidGuessError`**: A custom exception raised when a guess violates the game's rules.
- **`GuessingGame`**: Manages the secret number, validates guesses, provides feedback, tracks attempts, and updates the game state.
- **`play()`**: Runs the console game loop. Its input and output functions can be replaced for testing.
- **`main()`**: Allows players to start new rounds and choose whether to play again.

The game logic is separated from the console interface, making it easier to test individual features without requiring interactive keyboard input.

### `test_guessing_game.py`

The test file uses Python's built-in `unittest` framework to verify that the game works correctly.

Tests cover:

- Random secret number generation and range restrictions.
- Rejection of even, non-integer, and out-of-range guesses.
- Correct, too-high, and too-low guess results.
- Initial, playing, and won game states.
- Accurate attempt counting and exclusion of invalid guesses.
- Prevention of additional guesses after winning.
- Console behavior, including quitting, invalid input, and reporting the number of attempts.

Random seeds and fixed secret numbers make the tests repeatable and predictable.

## How to Run

**Start the game:**

```bash
python3 guessing_game.py
```

**Run all unit tests:**

```bash
python3 -m unittest
```

## Authors

Ayush, Kemi, Kyle
