from random import randint

from brain_games.utils import get_gcd


def brain_gcd():
    first_number = randint(0, 100)
    second_number = randint(0, 100)
    question = f"{ first_number } { second_number }"
    correct_answer = get_gcd(first_number, second_number)
    return question, str(correct_answer)
