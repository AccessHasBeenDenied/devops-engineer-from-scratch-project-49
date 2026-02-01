from brain_games.games.brain_calc import brain_calc
from brain_games.utils import run


def main():
    run(
        brain_calc,
        'What is the result of the expression?'
    )


if __name__ == "__main__":
    main()
