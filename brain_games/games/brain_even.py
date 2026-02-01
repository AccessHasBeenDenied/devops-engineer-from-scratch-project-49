from random import randint

from brain_games.utils import (
    is_even,
)


def brain_even():
    number = randint(0, 100)
    correct_answer = 'yes' if is_even(number) else 'no'
    return str(number), correct_answer