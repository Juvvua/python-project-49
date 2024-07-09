import random


TEXT = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


def get_correct_answer(question):
    if is_prime(question):
        return 'yes'
    return 'no'


def make_question_and_answer():
    question = random.randint(1, 100)
    correct_answer = get_correct_answer(question)
    return question, correct_answer
