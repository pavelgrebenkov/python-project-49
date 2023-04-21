from brain_games.games.all_games_code import comp_rand_num, user_response, name

#################################################
# This block of code instructs the user on how to play the game.


instruction = 'Answer "yes" if given number is prime. Otherwise answer "no".'
print(instruction)


##################################################
# This block of code makes decisions about the user’s responses.


def comp_decision():
    attempts_correct = 0

    while attempts_correct < 3:
        rand_num = comp_rand_num()
        question = f'Question: {rand_num}'
        print(question)

        prime_num = True
        non_prime_num = False

        def is_prime():
            if rand_num > 1:
                for i in range(2, rand_num):
                    if (rand_num % i) == 0:
                        return non_prime_num
                else:
                    return prime_num
            else:
                return non_prime_num

        player_response = user_response()

        yes = player_response.lower() == "yes"
        no = player_response.lower() == "no"

        if (is_prime() == yes and is_prime() != no):
            attempts_correct += 1
            print("Correct!")

        elif (is_prime() is True and is_prime() == no):
            print(f"No is wrong answer ;(. Let's try again, {name}!")
            return comp_decision()

        elif (is_prime() is False and is_prime() != yes):
            print(f"Yes is wrong answer ;(. Let's try again, {name}!")
            return comp_decision()

        else:
            print(f"Your answer isn't clear. ;(. Let's try again, {name}!")
            return comp_decision()

    print(f"Congratuations, {name}!")
