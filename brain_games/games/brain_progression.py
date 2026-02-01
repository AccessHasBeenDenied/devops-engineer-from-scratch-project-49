from random import randint

from brain_games.config import progression_count
from brain_games.utils import arithmetic_progression_elem


def brain_progression():
    start = randint(0, 10)
    step = randint(0, 10)
    hidden_item_number = randint(0, progression_count)
    question = " ".join(
        str(arithmetic_progression_elem(start, i, step))
        if i != hidden_item_number
        else ".."
        for i in range(0, progression_count)
    )
    correct_answer = arithmetic_progression_elem(
        start, hidden_item_number, step
    )
    return question, str(correct_answer)