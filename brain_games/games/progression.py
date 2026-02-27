# progression.py
"""Arithmetic progression game module.

In this game, the user is shown a random sequence of numbers
and must provide the missing number according to the rule of
progression.
"""
import random

from brain_games.games.utils import generate_number

ANSWER_TYPE = 'numeric'
INSTRUCTION = 'What number is missing in the progression?'


def generate_round():
    """Generate a question and its correct answer for the progression game.

    Returns:
        tuple: A pair containing (question_string, correct_answer_string)
               e.g., ("5 10 .. 20 25", "15")
    """
    # Each variable gets its own independent random value
    start = generate_number(1, 30)   # First number in sequence
    step = generate_number(2, 8)     # Difference between numbers
    length = generate_number(5, 10)  # How many numbers in sequence

    # Generate the arithmetic progression
    math_seq = []
    for i in range(1, length + 1):
        math_seq.append(start + i * step)

    index = random.randrange(len(math_seq))
    # Return as string for comparison
    correct_answer = str(math_seq[index])
    # Hide a random element
    math_seq[index] = ".."
    question = f"{' '.join(str(item) for item in math_seq)}"
    return (question, correct_answer)
