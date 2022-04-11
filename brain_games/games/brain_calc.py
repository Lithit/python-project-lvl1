import random

TASK = "What is the result of the expression?"

def brain_calc(num_1, exp, num_2):
    if exp == '+':
        return num_1 + num_2
    if exp == '-':
        return num_1 - num_2
    if exp == '*':
        return num_1 * num_2

def get_round():
    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    operators = ['+', '-', '*']
    exp = random.choice(operators)
    question = f"{num_1} {exp} {num_2}"
    answer = brain_calc(num_1, exp, num_2)
    return question, str(answer)
