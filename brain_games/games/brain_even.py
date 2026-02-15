from random import randint


def is_even(value):
    return not value % 2


def brain_even():
    rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    number = randint(0, 100)
    correct_answer = 'yes' if is_even(number) else 'no'
    return rule, str(number), correct_answer