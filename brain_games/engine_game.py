#!/usr/bin/env python

import prompt


def run_engine_game(games):
    print('Welcome to the Brain Games!')
    
    username = prompt.string('May I have your name? ')
    print('Hello,', username + '!')
    
    print(games.TASK)
    rounds_count = 3
    for i in range(rounds_count):
        question, answer = games.get_round()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer != answer:
            print(
                f"'{user_answer}' is wrong answer ;(."
                f" Correct answer was '{answer}'.\n"
                f"Let's try again, {username}!"
            )
        print('Correct!')
        return print(f"Congratulations, {username}!")