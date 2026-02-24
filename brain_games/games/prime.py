# prime.py
"""Prime number game module.

In this game, the user is shown a random number and
must determine if it is a prime or not.
"""


from brain_games.games.utils import generate_number


ANSWER_TYPE = 'yesno'
INSTRUCTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """Determine if a number is prime.

    Args:
        number (int): The number to check

    Returns:
        bool: True if the number is prime, False otherwise

    Example:
        >>> is_prime(3)
        True
        >>> is_prime(4)
        False
    """
    if number < 2:
        # 0 and 1 are not prime
        return False
    for i in range(2, number):
        if number % i == 0:
            # Found a factor, not prime
            return False
    # No factors found, it is prime
    return True


def generate_round():
    """Generate a question and its correct answer
        for the prime number game.


        Returns:
        tuple: A pair containing (question_string, correct_answer_string)
               e.g., ("3", "yes")
               e.g., ("4", "no")
    """
    number = generate_number()
    question = str(number)
    correct_answer = "yes" if is_prime(number) else "no"
    return (question, correct_answer)
