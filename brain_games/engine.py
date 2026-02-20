import prompt

from brain_games import constants

from .cli import welcome_user


def run(module):
    username = welcome_user()
    print(module.RULE)
    game_counter = constants.GAME_COUNT
    while game_counter:
        question, correct_answer = module.game()
        print(f"Question: { question }")
        answer = prompt.string("Answer: ")
        if answer == correct_answer:
            print("Correct!")
            game_counter = game_counter - 1
        else:
            print(
                f"'{ answer }' is wrong answer ;(." 
                f"Correct answer was '{ correct_answer }'."
            )
            print(f"Let's try again, { username }!")
            return
    else:
        print(f"Congratulations, { username }!")