from brain_games.engine import run
from brain_games.games.brain_calc import RULE, brain_calc


def main():
    run(brain_calc, RULE)


if __name__ == "__main__":
    main()
