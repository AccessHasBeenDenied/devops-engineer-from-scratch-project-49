from random import randint

from brain_games.constants import PROGRESSION_COUNT

RULE = 'What number is missing in the progression?'


def arithmetic_progression_elem(start, index, step):
    return start + index * step


def brain_progression():
    start = randint(0, 10)
    step = randint(0, 10)
    hidden_item_number = randint(0, PROGRESSION_COUNT - 1)
    question = " ".join(
        str(arithmetic_progression_elem(start, i, step))
        if i != hidden_item_number
        else ".."
        for i in range(0, PROGRESSION_COUNT)
    )
    correct_answer = arithmetic_progression_elem(
        start, hidden_item_number, step
    )
    return question, str(correct_answer)