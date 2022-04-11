#!/usr/bin/env python

import prompt

ROUNDS = 3


def welcome():
    print('Welcome to the Brain Games!')


def get_username():
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    return name


def get_engine_game(games):
    welcome()
    username = get_username()
    print(games.TASK)
    for i in range(ROUNDS):
        question, answer = games.get_round()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'. "
                f"Let's try again, {username}!"
            )
            return
        print(f"Congratulations, {username}!")
