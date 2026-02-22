# even.py
from brain_games.games.utils import generate_number

ANSWER_TYPE = 'yesno'
INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    """Generate a question and its correct answer."""
    number = generate_number()
    question = str(number)
    correct_answer = "yes" if number % 2 == 0 else "no"
    return (question, correct_answer)
