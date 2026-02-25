# utils.py
"""The utility module provides helper functions for the game engine and game modules.

Functions:
- 'is_valid_answer': checks if a user answer is valid for the game type - numeric or yesno.
- 'normalize_answer': brings all answers for the 'yesno' game types to lower case.
- 'get_user_answer': receives user answer inputs.
- 'generate_number': generates random numbers in the range of five to ten.

NOTE: The engine imports the first three functions; the game modules import the last function.
"""


import prompt
import random


def is_valid_answer(answer, answer_type):
    """Check if answer is valid for the game type.


    Args:
        answer (str): The user's input answer.
        answer_type (str): Either 'numeric' or 'yesno'.

    Returns:
        bool: True if answer is valid for the game type, False otherwise.

    Example:
        >>> is_valid_answer("42", "numeric")
        True
        >>> is_valid_answer("042", "numeric")
        False
        >>> is_valid_answer("a_string", "numeric")
        False
        >>> is_valid_answer("yes", "yesno")
        True
        >>> is_valid_answer("no", "yesno")
        True
        >>> is_valid_answer("42", "yesno")
        False
    """
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
    """Convert answer to standard format for comparison.


    Args:
        answer (str): The user's input answer.
        answer_type (str): Either 'numeric' or 'yesno'.

    Returns:
        str: If answer is numeric, return string itself. If 'yesno' answer,
        convert to lower case if any character is upper case
        or return string itself.

    Example:
        >>> normalize_answer("yes", "yesno")
        "yes"
        >>> normalize_answer("Yes", "yesno")
        "yes"
    """
    if answer_type == 'yesno':
        # Convert to lower case to normalize
        return answer.lower()
    return answer


def get_user_answer():
    """Get and return user's answer as string.


    Returns:
        str: The input string provided by the user.

    Example:
        >>> user_answer = get_user_answer()
        Your answer: Jack
    """
    return prompt.string('Your answer: ')


def generate_number(min_val=5, max_val=10):
    """Generate a random number between min_val and max_val, inclusive.

    Args:
        min_val (int, optional): The minimum possible value for the generated number.
        max_val (int, optional): The maximum possible value for the generated number.

    Returns:
        int: A random integer between min_val and max_val.

    Example:
        >>> generate_number(1, 5)
        3  # Output will vary
    """
    return random.randint(min_val, max_val)
