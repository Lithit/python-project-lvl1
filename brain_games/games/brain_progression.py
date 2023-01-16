import random
from random import randint

TASK = "What number is missing in the progression?"


def get_question_answer():
    start = randint(1, 50)
    step = randint(1, 20)
    length_progression = 10
    
    end = start + length_progression * step
    progression = list(range(start, end, step))
    index = random.randrange(1, length_progression)
    
    answer = progression[index]
    progression[index] = '..'
    question = ' '.join(map(str, progression))
    return question, str(answer)
