#!/usr/bin/env python3

from random import randint

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_round():
    question = randint(1, 100)
    answer = 'no' if question % 2 else 'yes'
    return str(question), str(answer)
