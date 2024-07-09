import prompt

TRIES_COUNT = 3


def run(game_text, make_question_and_answer):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_text)
    for n in range(TRIES_COUNT):
        question, correct_answer = make_question_and_answer()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
        if n == TRIES_COUNT - 1:
            print(f'Congratulations, {name}!')
