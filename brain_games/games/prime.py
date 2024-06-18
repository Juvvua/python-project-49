import random


TEXT = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_correct_answer(question):
    if question < 2:
        return 'no'
    for i in range(2, question):
        if question % i == 0:
            return 'no'
    return 'yes'


def make_question_and_answer():
    question = random.randint(1, 100)
    correct_answer = get_correct_answer(question)
    return question, correct_answer