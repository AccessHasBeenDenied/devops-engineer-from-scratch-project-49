from random import randint


def get_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def brain_gcd():
    rule = 'Find the greatest common divisor of given numbers.'
    first_number = randint(0, 100)
    second_number = randint(0, 100)
    question = f"{ first_number } { second_number }"
    correct_answer = get_gcd(first_number, second_number)
    return rule, question, str(correct_answer)
