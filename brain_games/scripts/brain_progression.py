from brain_games.games.brain_progression import brain_progression
from brain_games.utils import run


def main():
    run(
        brain_progression,
        'What number is missing in the progression?'
    )


if __name__ == "__main__":
    main()
