# gcd.py
"""Greatest common divisor (gcd) game module.

In this game, the user is shown a random pair of numbers
and must provide their gcd.
"""


import math
from brain_games.games.utils import generate_number

ANSWER_TYPE = 'numeric'
INSTRUCTION = 'Find the greatest common divisor of given numbers.'


def generate_round():
    """Generate a question and its correct answer for the gcd game.

    Returns:
        tuple: A pair containing (question_string, correct_answer_string)
               e.g., ("5 10", "5")
    """
    num1 = generate_number()
    num2 = generate_number()
    question = f"{num1} {num2}"
    # Return as string for comparison
    correct_answer = str(math.gcd(num1, num2))
    return (question, correct_answer)
