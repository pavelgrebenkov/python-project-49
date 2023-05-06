import math
from brain_games.games.all_games_code import comp_rand_num, user_response, name

#################################################
# This block of code instructs the user on how to play the game.


instruction = 'Find the greatest common divisor of given numbers.'
print(instruction)

#################################################
# This block of code makes decisions about the user’s responses.


def comp_question():
    rand_num_1 = comp_rand_num()
    rand_num_2 = comp_rand_num()
    rand_num_pair = f'{rand_num_1} {rand_num_2}'
    question = f'Question: {rand_num_pair}'
    print(question)
    gcd = math.gcd(rand_num_1, rand_num_2)
    return gcd


def comp_decision():
    attempts_correct = 0

    while attempts_correct < 3:
        gcd = comp_question()

        try:
            ans = int(user_response())

        except ValueError:
            print(f"""Your answer isn't clear. ;(.
Let's try again {name}!""")
            # attempts_correct = 0
            return

        if gcd == ans:
            attempts_correct += 1
            print("Correct!")

        else:
            print(f"""'{ans}' is wrong answer ;(. Correct answer was '{gcd}'.
Let's try again, {name}!""")
            # attempts_correct = 0
            return

    print(f"Congratuations, {name}!")
