from brain_games.games.brain_even import brain_even
from brain_games.utils import run


def main():
    run(
        brain_even,
        'Answer "yes" if the number is even, otherwise answer "no".'
    )


if __name__ == "__main__":
    main()
