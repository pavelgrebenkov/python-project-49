# utils.py

import prompt
import random


def is_valid_answer(answer, answer_type):
    """Check if answer is valid for the game type."""
    if answer_type == 'numeric':
        # Check for leading zeros
        if answer.startswith('0') and len(answer) > 1:
            return False
        try:
            int(answer)
            return True
        except ValueError:
            return False
    elif answer_type == 'yesno':
        return answer.lower() in ['yes', 'no']
    return True


def normalize_answer(answer, answer_type):
    """Convert answer to standard format for comparison."""
    if answer_type == 'yesno':
        # Convert to lower case to normalize
        return answer.lower()
    return answer


def generate_number(min_val=5, max_val=10):
    """Generate a random number between min_val and max_val."""
    return random.randint(min_val, max_val)


def get_user_answer():
    """Get and return user's answer as string."""
    return prompt.string('Your answer: ')
