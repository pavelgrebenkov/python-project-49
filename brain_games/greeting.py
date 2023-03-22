# This function welcomes the user, asks for his/her name and greets him/her.
# This function is the same for all games.

import prompt


def greet_user():
    print('Welcome to the Brain Games')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
