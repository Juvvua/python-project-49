import random


TEXT = 'What number is missing in the progression?'


def get_random_progression():
    length = random.randint(5, 10)
    step = random.randint(2, 5)
    start = random.randint(1, 10)
    stop = start + step * length
    return list(range(start, stop + 1, step))


def make_question_and_answer():
    numbers = get_random_progression()
    cut = random.randint(0, len(numbers) - 1)
    correct_answer = numbers[cut]
    numbers[cut] = '..'
    for n in range(len(numbers)):
        numbers[n] = str(numbers[n])
    question = ' '.join(numbers)
    return question, str(correct_answer)
