#!/usr/bin/env python3

import random

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no"'


def is_prime(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


def get_question_answer():
    num = random.randint(2, 60)
    answer = 'yes' if is_prime(num) else 'no'
    return str(num), str(answer)
