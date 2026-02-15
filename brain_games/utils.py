import prompt

from brain_games import config


def greet():
    print('Welcome to the Brain Games!')


def welcome_user():
    username = prompt.string("May I have your name? ")
    print(f"Hello, { username }!")
    return username


def run(game):
    username = welcome_user()
    rule, _, _ = game()
    print(rule)
    while config.game_count:
        _, question, correct_answer = game()
        print(f"Question: { question }")
        answer = prompt.string("Answer: ")
        if answer == correct_answer:
            print("Correct!")
            config.game_count = config.game_count - 1
        else:
            print(
                f"'{ answer }' is wrong answer ;(." 
                f"Correct answer was '{ correct_answer }'."
            )
            print(f"Let's try again, { username }!")
            break
    else:
        print(f"Congratulations, { username }!")