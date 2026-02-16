from brain_games.engine import run
from brain_games.games.brain_progression import RULE, brain_progression


def main():
    run(brain_progression, RULE)


if __name__ == "__main__":
    main()
