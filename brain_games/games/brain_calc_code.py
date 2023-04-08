import random
from brain_games.games.all_games_code import comp_rand_num, user_response, name

#################################################
# This block of code instructs the user on how to play the game.


instruction = 'What is the result of the expression?'
print(instruction)

#################################################
# This block of code makes decisions about the user’s responses.


def comp_decision():
    attempts_correct = 0

    while attempts_correct < 3:
        rand_num = comp_rand_num()
        math_opr = ('+', '-', '*')
        rand_math_opr = random.choice(math_opr)
        rand_math_expr = f'{rand_num} {rand_math_opr} {rand_num}'
        question = f'Question: {rand_math_expr}'
        print(question)

        math_expr_result = eval(rand_math_expr)

        try:
            player_response = int(user_response())

        except ValueError:
            print(f"Your answer isn't clear. ;(. Let's try again {name}!")
            return comp_decision()

        if math_expr_result == player_response:
            attempts_correct += 1
            print("Correct!")

        if math_expr_result != player_response:
            print(f"""{player_response} is wrong answer ;(.
Correct answer was {math_expr_result}.
Let's try again, {name}!""")
            return comp_decision()

    print(f"Congratuations, {name}!")
