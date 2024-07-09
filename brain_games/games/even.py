import random


TEXT = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_correct_answer(question):
    if is_even(question):
        return 'yes'
    return 'no'


def make_question_and_answer():
    question = random.randint(0, 100)
    correct_answer = get_correct_answer(question)
    return question, correct_answer
