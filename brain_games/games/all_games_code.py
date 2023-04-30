#################################################
# This file contains code common to all the brain games.

import prompt
import random

#################################################
# This block of code welcomes the user and asks for his/her name.


def welcome_user():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


welcome_user()

#################################################
# This block of code generates random numbers.


def comp_rand_num():
    rand_num = random.randint(5, 10)
    return rand_num

#################################################
# This block of code receives the user’s responses.


def user_response():
    answer = prompt.string('Your answer: ')
    return answer
