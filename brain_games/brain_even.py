from random import randint

import prompt

from brain_games import config


def is_even(value):
    return not value % 2


def print_success():
    print("Yes!")


def print_failed(answer, correct_answer):
    print(
        f"'{ answer }' is wrong answer ;(." 
        f"Correct answer was '{ correct_answer }'."
    )
    print(f"Let's try again, { config.username }!")


def print_congrats():
    print(f"Congratulations, { config.username }!")


def brain_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')

    while config.game_count:
        number = randint(0, 100)
        correct_answer = 'yes' if is_even(number) else 'no'
        print(f"Question: { number }")
        answer = prompt.string("Answer: ")
        if answer == correct_answer:
            print_success()
            config.game_count = config.game_count - 1
        else:
            print_failed(answer, correct_answer)
            break
    else:
        print_congrats()