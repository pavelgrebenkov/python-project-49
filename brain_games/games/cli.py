# cli.py
"""
- This is the user-interface module that launches the games.
- Its main purpose is to welcome the user and ask for their name.
- It is imported into every script of each game.
"""


import prompt


def welcome_user():
    """Display welcome message, prompt for name, and return it."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
