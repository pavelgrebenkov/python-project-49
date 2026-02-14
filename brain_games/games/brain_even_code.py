from brain_games.games.all_games_code import comp_rand_num, user_response


def comp_question():
    rand_num = comp_rand_num()
    question = f'Question: {rand_num}'
    print(question)
    return rand_num


def comp_decision(name):
    instruction = 'Answer "yes" if the number is even, otherwise answer "no".'
    print(instruction)

    attempts_correct = 0

    while attempts_correct < 3:
        question = comp_question()
        player_response = user_response()

        num_even = (question % 2 == 0)

        yes = bool(player_response.lower() == "yes")
        no = bool(player_response.lower() == "no")

        if (num_even == yes and num_even != no):
            attempts_correct += 1
            print("Correct!")

        elif (num_even is False and yes):
            print(f"""'yes' is wrong answer. Correct answer was 'no'.
Let's try again, {name}!""")
            # attempts_correct = 0
            return

        elif (num_even is True and no):
            print(f"""'no' is wrong answer. Correct answer was 'yes'.
Let's try again, {name}!""")
            # attempts_correct = 0
            return

        else:
            print(f"""Your answer isn't clear.
Let's try again, {name}!""")
            # attempts_correct = 0
            return

    print(f"Congratulations, {name}!")
