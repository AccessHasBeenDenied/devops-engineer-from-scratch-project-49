import prompt

from brain_games import config


def greet():
    print('Welcome to the Brain Games!')


def welcome_user():
    username = prompt.string("May I have your name? ")
    print(f"Hello, { config.username }!")
    return username


def is_even(value):
    return not value % 2


def print_success():
    print("Correct!")


def print_failed(answer, correct_answer, username):
    print(
        f"'{ answer }' is wrong answer ;(." 
        f"Correct answer was '{ correct_answer }'."
    )
    print(f"Let's try again, { username }!")


def print_congrats(username):
    print(f"Congratulations, { username }!")


def run(game, rule):
    greet()
    username = welcome_user()
    print(rule)
    while config.game_count:
        question, correct_answer = game()
        print(f"Question: { question }")
        answer = prompt.string("Answer: ")
        if answer == correct_answer:
            print_success()
            config.game_count = config.game_count - 1
        else:
            print_failed(answer, correct_answer, username)
            break
    else:
        print_congrats(username)