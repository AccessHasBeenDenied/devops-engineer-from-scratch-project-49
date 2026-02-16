from brain_games.engine import run
from brain_games.games.brain_prime import RULE, brain_prime


def main():
    run(brain_prime, RULE)


if __name__ == "__main__":
    main()
