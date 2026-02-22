# calc.py
import random
from brain_games.games.utils import generate_number

ANSWER_TYPE = 'numeric'  
INSTRUCTION = 'What is the result of the expression?'

def generate_round():
    num1 = generate_number()
    num2 = generate_number()
    operator = random.choice(('+', '-', '*'))
    question = f"{num1} {operator} {num2}"
    correct_answer = str(eval(f"{num1}{operator}{num2}"))  # Return as string for comparison
    return (question, correct_answer)
