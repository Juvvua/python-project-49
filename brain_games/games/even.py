import random


TEXT = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_correct_answer(question):
    if question % 2 == 0:
        return 'yes'
    return 'no'


def make_question_and_answer():
    question = random.randint(0, 100)
    correct_answer = get_correct_answer(question)
    return question, correct_answer
