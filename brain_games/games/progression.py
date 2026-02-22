# progression.py
import random
from brain_games.games.utils import generate_number

ANSWER_TYPE = 'numeric'  
INSTRUCTION = 'What number is missing in the progression?'

def generate_round():
    math_seq = []
    number = generate_number()
    for i in range(1, number + 1):
        math_seq.append(number + (i - 1) * number)
    index = random.randrange(len(math_seq))
    correct_answer = str(math_seq[index]) # Return as string for comparison
    math_seq[index] = ".."            
    question = f"{' '.join(str(item) for item in math_seq)}"
    return (question, correct_answer)
