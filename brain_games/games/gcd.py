# gcd.py
import math
from brain_games.games.utils import generate_number

ANSWER_TYPE = 'numeric'  
INSTRUCTION = 'Find the greatest common divisor of given numbers.'


def generate_round():
    num1 = generate_number()
    num2 = generate_number()
    question = f"{num1} {num2}"
    correct_answer = str(math.gcd(num1, num2)) # Return as string for comparison
    return (question, correct_answer)
