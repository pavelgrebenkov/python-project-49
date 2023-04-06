import random
import prompt
from brain_games.greeting import name

#################################################
# This block of code instructs the user on how to play the game.


instruction = 'What is the result of the expression?'
print(instruction)

#################################################
# This block of code generates random numbers.


def comp_random_number():
    random_num = random.randint(1, 10)
    return random_num

#################################################
# This block of code receives the user’s responses.


def user_response():
    answer = prompt.string('Your answer: ')
    return answer

#################################################
# This block of code makes decisions about the user’s responses.


def comp_decision():
    attempts_correct = 0

    while attempts_correct < 3:
        random_num = comp_random_number()
        math_operators = ('+', '-', '*')
        random_math_operators = random.choice(math_operators)
        random_math_expression = f'{random_num} {random_math_operators} {random_num}'
        question = f'Question: {random_math_expression}'
        print(question)

        math_expression_result = eval(random_math_expression)
        player_response = int(user_response())

        if math_expression_result == player_response:
            attempts_correct += 1
            print("Correct!")

        if math_expression_result != player_response:
            print(f"{player_response} is wrong answer ;(. Correct answer was {math_expression_result}. Let's try again, {name}!")
            return comp_decision()

    print(f"Congratuations, {name}!")
