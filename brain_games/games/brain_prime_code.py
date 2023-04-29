from brain_games.games.all_games_code import comp_rand_num, user_response, name

#################################################
# This block of code instructs the user on how to play the game.


instruction = 'Answer "yes" if given number is prime. Otherwise answer "no".'
print(instruction)


##################################################
# This block of code makes decisions about the user’s responses.


def comp_question():
    rand_num = comp_rand_num()
    question = f'Question: {rand_num}'
    print(question)

    for i in range(2, rand_num):
        if (rand_num % i) == 0:
            return False
    else:
        return True


def comp_decision():
    attempts_correct = 0

    while attempts_correct < 3:
        prime_num = comp_question()

        player_response = user_response()

        yes = bool(player_response.lower() == "yes")
        no = bool(player_response.lower() == "no")

        if (prime_num == yes and prime_num != no):
            attempts_correct += 1
            print("Correct!")

        elif (prime_num is True and no):
            print(f"No is wrong answer ;(. Let's try again, {name}!")
            attempts_correct = 0
            continue

        elif (prime_num is False and yes):
            print(f"Yes is wrong answer ;(. Let's try again, {name}!")
            attempts_correct = 0
            continue

        else:
            print(f"Your answer isn't clear. ;(. Let's try again, {name}!")
            attempts_correct = 0
            continue

    print(f"Congratuations, {name}!")
