import random
from brain_games.games.all_games_code import comp_rand_num, user_response, name

#################################################
# This block of code instructs the user on how to play the game.


instruction = 'What number is missing in the progression?'
print(instruction)

#################################################
# This block of code makes decisions about the user’s responses.


def comp_decision():
    attempts_correct = 0

    while attempts_correct < 3:
        rand_math_seq = []
        rand_num = comp_rand_num()

        for i in range(1, rand_num + 1):
            rand_math_seq.append(rand_num + (i - 1) * rand_num)

        elem = ".."
        rand_index = random.randrange(len(rand_math_seq))
        correct_answer = rand_math_seq[rand_index]
        rand_math_seq[rand_index] = elem

        question = f'Question: {str(rand_math_seq)[1 : -1]}'
        print(question)

        try:
            player_response = int(user_response())

        except ValueError:
            print(f"Your answer isn't clear. ;(. Let's try again {name}!")
            return comp_decision()

        if correct_answer == player_response:
            attempts_correct += 1
            print("Correct!")

        if correct_answer != player_response:
            print(f"""{player_response} is wrong answer ;(.
Correct answer was {correct_answer}.
Let's try again, {name}!""")
            return comp_decision()

    print(f"Congratuations, {name}!")
