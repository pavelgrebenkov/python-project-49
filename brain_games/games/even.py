# even.py
"""Even number game module.

In this game, the user is shown a random number and
must determine if it is even or odd.
"""


from brain_games.games.utils import generate_number

ANSWER_TYPE = 'yesno'
INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    """Generate a question and its correct answer for the even number game.


    Returns:
        tuple: A pair containing (question_string, correct_answer_string)
               e.g., ("4", "yes")
               e.g., ("5", "no")
    """
    number = generate_number()
    question = str(number)
    correct_answer = "yes" if number % 2 == 0 else "no"
    return (question, correct_answer)
