import prompt


def welcome_user():
    """Display welcome message, prompt for name, and return it."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
