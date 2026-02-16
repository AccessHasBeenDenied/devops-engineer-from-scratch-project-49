from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(value):
    return not value % 2


def brain_even():
    number = randint(0, 100)
    correct_answer = 'yes' if is_even(number) else 'no'
    return str(number), correct_answer