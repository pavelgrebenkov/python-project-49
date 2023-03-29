import random

#################################################
# This block of code instructs the user on how to play the game.


def comp_instruction():
    instruction = 'Answer "yes" if the number is even, otherwise answer "no".'
    print(instruction)
    # return instruction


comp_instruction()


#################################################
# This block of code generates random numbers.


def comp_random_number():
    random_num = random.randint(1, 100)
    # print(random_num)
    return random_num


# comp_random_number()


#################################################
# This block of code receives the user’s responses.


def user_response():
    answer = input('Your answer: ')
    # print(answer)
    return answer


# user_response()


#################################################
# This block of code makes decisions about the user’s responses.


def comp_decision():
    # comp_instruction()
    attempts_correct = 0
    attempts_incorrect = 0

    while attempts_correct < 3:
        random_num = comp_random_number()
        question = f'Question: {random_num}'
        print(question)
        player_response = user_response()
        num_even = (random_num % 2 == 0)
        num_odd = (random_num % 2 != 0)
        yes = bool(player_response.lower() == "yes")
        no = bool(player_response.lower() == "no")

        if (num_even == yes or num_odd == no):
            attempts_correct += 1
            print("Correct!")
            continue

        while attempts_incorrect == 0:

            if num_even == no or num_odd == yes:
                attempts_incorrect += 1
                print("Try again!")
                return comp_decision()

    print("Congratuations, player!")


comp_decision()
