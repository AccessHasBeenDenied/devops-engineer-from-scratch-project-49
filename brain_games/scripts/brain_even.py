from brain_games.engine import run
from brain_games.games.brain_even import RULE, brain_even


def main():
    run(brain_even, RULE)


if __name__ == "__main__":
    main()
