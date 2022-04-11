
from random import randint

TASK = "What number is missing in the progression?"

def prog(start, step, lenght_pr):
    result = [start]
    x = 0
    while x < lenght_pr:
        start = start + step
        result.append(start)
        x = x + 1
    return result

def get_round():
    start = randint(1, 30)
    step = randint(1, 5)
    lenght_pr = randint(6, 9)
    f_num = prog(start, step, lenght_pr)
    index = randint(0, lenght_pr)
    answer = f_num[index]
    f_num[index] = '..'
    question = ' '.join(map(str, f_num))
    return question, str(answer)
