from brain_games.games.brain_gcd import brain_gcd
from brain_games.utils import run


def main():
    run(
        brain_gcd,
        'Find the greatest common divisor of given numbers.'
    )


if __name__ == "__main__":
    main()
