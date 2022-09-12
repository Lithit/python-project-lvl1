import random
import operator
TASK = "What is the result of the expression?"

def get_round():
    operand1 = random.randint(1, 10)
    operand2 = random.randint(1, 10)
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    operation = random.choice(list(operations.keys()))
    answer = str(operations[operation](operand1, operand2))
    question = f"{operand1} {operation} {operand2}"
    return question, answer
