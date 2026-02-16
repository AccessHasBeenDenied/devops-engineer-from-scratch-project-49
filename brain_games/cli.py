import prompt

from brain_games import constants


def welcome_user():
    constants.username = prompt.string("May I have your name? ")
    print(f"Hello, { constants.username }!")
