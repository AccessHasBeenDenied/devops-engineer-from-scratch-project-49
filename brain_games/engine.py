import prompt

from brain_games import constants


def greet():
    print('Welcome to the Brain Games!')


def welcome_user():
    username = prompt.string("May I have your name? ")
    print(f"Hello, { username }!")
    return username


def run(game, rule):
    username = welcome_user()
    print(rule)
    while constants.GAME_COUNT:
        question, correct_answer = game()
        print(f"Question: { question }")
        answer = prompt.string("Answer: ")
        if answer == correct_answer:
            print("Correct!")
            constants.GAME_COUNT = constants.GAME_COUNT - 1
        else:
            print(
                f"'{ answer }' is wrong answer ;(." 
                f"Correct answer was '{ correct_answer }'."
            )
            print(f"Let's try again, { username }!")
            break
    else:
        print(f"Congratulations, { username }!")