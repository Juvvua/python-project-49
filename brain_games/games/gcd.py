import random


TEXT = 'Find the greatest common divisor of given numbers.'


def get_gcd(number1, number2):
    divisor = 1
    for n in range(1, number1 + 1):
        if number1 % n == 0 and number2 % n == 0:
            divisor = n
    return divisor


def make_question_and_answer():
    number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)
    question = f'{number1} {number2}'
    correct_answer = get_gcd(number1, number2)
    return question, str(correct_answer)
