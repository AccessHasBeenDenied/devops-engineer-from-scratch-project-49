from random import randint


def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def brain_prime():
    rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    number = randint(0, 1000)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return rule, str(number), correct_answer
