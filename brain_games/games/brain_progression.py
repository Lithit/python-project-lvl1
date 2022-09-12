
from random import randint

TASK = "What number is missing in the progression?"

def get_round():
    start = randint(1, 30)
    step = randint(1, 5)
    lenght_pr = randint(6, 9)
    progression = list(range(start, (start + lenght_pr * step), step))
    index = randint(0, lenght_pr)
    answer = progression[index]
    progression[index] = '..'
    question = ' '.join(map(str, progression))
    return question, str(answer)
