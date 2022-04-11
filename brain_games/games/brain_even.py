#!/usr/bin/env python3

from random import randint

TASK = ('Answer "yes" if the number is even, otherwise answer "no".')

def get_round():
    n = randint(1, 100)
    if n % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return str(n), str(answer)
