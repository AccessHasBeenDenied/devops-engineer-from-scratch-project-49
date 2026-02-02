from random import randint

from brain_games.utils import is_prime


def brain_prime():
    number = randint(0, 1000)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return str(number), correct_answer
