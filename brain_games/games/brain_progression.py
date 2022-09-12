from random import randint

TASK = "What number is missing in the progression?"


def get_round():
    start = randint(1, 50)
    step = randint(1, 20)
    lenght_pr = 10
    progression = list(range(start, (start + lenght_pr * step), step))
    index = randint(0, len(progression))
    answer = progression[index]
    progression[index] = '..'
    question = ' '.join(map(str, progression))
    return question, str(answer)
