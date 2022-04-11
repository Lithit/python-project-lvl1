import random

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no"'

def brain_prime(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True

def get_round():
    num = random.randint(2, 60)
    answer = 'yes' if brain_prime(num) else 'no'
    return str(num), str(answer)
