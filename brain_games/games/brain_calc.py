from random import choice, randint

RULE = 'What is the result of the expression?'


def game():
    first_number = randint(0, 100)
    second_number = randint(0, 100)
    operation = choice(['+', '-', '*'])
    question = f"{ first_number } { operation } { second_number }"
    match operation:
        case '+':
            correct_answer = first_number + second_number
        case '-':
            correct_answer = first_number - second_number
        case '*':
            correct_answer = first_number * second_number

    return question, str(correct_answer)