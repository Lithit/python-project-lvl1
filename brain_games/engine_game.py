#!/usr/bin/env python

import prompt


def get_engine_game(games):
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print('Hello,', username + '!')
    print(games.TASK)
    rounds_count = 3
    for i in range(rounds_count):
        question, answer = games.get_round()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
        if user_answer != answer:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'. "
                f"Let's try again, {username}!"
            )
            return
        print(f"Congratulations, {username}!")
