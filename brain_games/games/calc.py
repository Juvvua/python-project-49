import random


PROCEDURES = ['+', '-', '*']
TEXT = 'What is the result of the expression?'


def get_correct_answer(number1, procedure, number2):
    if procedure == '+':
        return number1 + number2
    elif procedure == '-':
        return number1 - number2
    else:
        return number1 * number2


def make_question_and_answer():
    number1 = random.randint(0, 100)
    procedure = random.choice(PROCEDURES)
    number2 = random.randint(0, 100)
    question = f'{number1} {procedure} {number2}'
    correct_answer = get_correct_answer(number1, procedure, number2)
    return question, str(correct_answer)
