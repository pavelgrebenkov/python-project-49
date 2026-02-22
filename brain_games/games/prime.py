# prime.py
from brain_games.games.utils import generate_number

ANSWER_TYPE = 'yesno'  
INSTRUCTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def is_prime(number):
    """Check if a number is prime."""
    if number < 2:
        return False # 0 and 1 are not prime
    for i in range(2, number):
        if number % i == 0:
            return False # Found a factor, not prime
    return True # No factors found, it is prime

def generate_round():
    """Generate a prime-related question for the game round."""
    number = generate_number()
    question = str(number)
    correct_answer = "yes" if is_prime(number) else "no"
    return (question, correct_answer)
