import random


TEXT = 'What number is missing in the progression?'


def make_question_and_answer():
    length = random.randint(5, 10)
    step = random.randint(2, 5)
    start = random.randint(1, 10)
    stop = start + step * length
    numbers = list(range(start, stop + 1, step))
    cut = random.randint(0, len(numbers) - 1)
    correct_answer = numbers[cut]
    numbers[cut] = '..'
    for n in range(len(numbers)):
        numbers[n] = str(numbers[n])
    question = ' '.join(numbers)
    return question, str(correct_answer)
