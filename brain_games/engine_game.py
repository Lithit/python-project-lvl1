#!/usr/bin/env python

import prompt
from brain_games.cli import welcome_user


def run_engine_game(games):
    username = welcome_user()
    print(games.TASK)
    rounds_count = 3
    for i in range(rounds_count):
        question, answer = games.get_question_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer != answer:
            print(
                f"'{user_answer}' is wrong answer ;(."
                f" Correct answer was '{answer}'.\n"
                f"Let's try again, {username}!"
            )
            break
        print("Correct!")
    else:
        print(f"Congratulations, {username}!")
