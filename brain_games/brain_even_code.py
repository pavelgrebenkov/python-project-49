import random
import prompt
from brain_games.greeting import name

#################################################
# This block of code instructs the user on how to play the game.

instruction = 'Answer "yes" if the number is even, otherwise answer "no".'
print(instruction)

#################################################
# This block of code generates random numbers.


def comp_random_number():
    random_num = random.randint(1, 100)
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
        question = f'Question: {random_num}'
        print(question)

        player_response = user_response()

        num_even = (random_num % 2 == 0)
        num_odd = (random_num % 2 != 0)

        yes = bool(player_response.lower() == "yes")
        no = bool(player_response.lower() == "no")

        if (num_even == yes and num_odd == no):
            attempts_correct += 1
            print("Correct!")

        elif (num_odd is True and num_even != yes):
            print(f"Yes is wrong answer ;(. Let's try again, {name}!")
            return comp_decision()

        elif (num_even is True and num_odd != no):
            print(f"No is wrong answer ;(. Let's try again, {name}!")
            return comp_decision()

        else:
            print(f"Your answer isn't clear. ;(. Let's try again, {name}!")
            return comp_decision()

    print(f"Congratuations, {name}!")
