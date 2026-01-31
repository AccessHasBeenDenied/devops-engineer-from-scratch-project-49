import prompt

from brain_games import config


def welcome_user():
    config.username = prompt.string("May I have your name? ")
    print(f"Hello, { config.username }!")
