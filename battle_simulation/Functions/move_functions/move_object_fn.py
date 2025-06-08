from battle_simulation.Class.Move import Move
from battle_simulation.Functions.move_functions.category_check import category_check


def future_sight() -> Move:
    move_type='Psychic'
    move=Move('Future Sight',80,15,move_type,90,category_check(move_type))
    return move

def doom_desire() -> Move:
    move_type='Steel'
    move=Move('Doom Desire',80,15,move_type,90,category_check(move_type))
    return move