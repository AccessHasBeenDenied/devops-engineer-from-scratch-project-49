from brain_games.games.brain_prime import brain_prime
from brain_games.utils import run


def main():
    run(
        brain_prime,
        'Answer "yes" if given number is prime. Otherwise answer "no".'
    )


if __name__ == "__main__":
    main()
