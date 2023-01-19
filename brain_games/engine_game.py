#!/usr/bin/env python

import prompt


def run_engine_game(games):
    print('Welcome to the Brain Games!')
    
    username = prompt.string('May I have your name? ')
    print('Hello,', username + '!')
    
    print(games.TASK)
    
    rounds_count = 3
    
    for i in range(rounds_count):
        question, answer = games.get_question_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        print("Correct!")
        
        if user_answer != answer:
            print(
            f"'{user_answer}' is wrong answer ;(."
            f" Correct answer was '{answer}'.\n"
            f"Let's try again, {username}!")
            break

        elif i == rounds_count - 1:
            print(f"Congratulations, {username}!")