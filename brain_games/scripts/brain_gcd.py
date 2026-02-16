from brain_games.engine import run
from brain_games.games.brain_gcd import RULE, brain_gcd


def main():
    run(brain_gcd, RULE)


if __name__ == "__main__":
    main()
