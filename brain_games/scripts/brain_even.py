from brain_games.brain_even import brain_even
from brain_games.cli import welcome_user
from brain_games.module import greet


def main():
    greet()
    welcome_user()
    brain_even()


if __name__ == "__main__":
    main()
