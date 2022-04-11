import random
import math

TASK = "Find the greatest common divisor of given numbers."
    
def get_round():
    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    answer = math.gcd(num_1, num_2)
    question = f"{num_1} {num_2}"
    return question, str(answer)
