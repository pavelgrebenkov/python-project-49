# calc.py
"""Calculator game module.

In this game, the user is shown a random arithmetic expression
(addition, subtraction, or multiplication) and must provide the correct result.
"""


import random

from brain_games.games.utils import generate_number

ANSWER_TYPE = 'numeric'
INSTRUCTION = 'What is the result of the expression?'


def generate_round():
    """Generate a question and its correct answer for the calculator game.

    Returns:
        tuple: A pair containing (question_string, correct_answer_string)
               e.g., ("5 + 3", "8")
    """
    num1 = generate_number()
    num2 = generate_number()
    operator = random.choice(('+', '-', '*'))
    question = f"{num1} {operator} {num2}"
    # Return as string for comparison
    correct_answer = str(eval(f"{num1}{operator}{num2}"))
    return (question, correct_answer)
