
from battle_simulation.Class.Move import Move
from battle_simulation.Class.Trainer import Trainer


def screen_calc(trainer: Trainer, battle_mode: int, move: Move, crit: bool) -> float:
    """Calculates the damage reduction multiplier due to Reflect or Light Screen effects, considering critical hits.

    Determines the damage multiplier for a move based on whether the defending trainer has 
    active screen effects:
    - **Reflect** reduces damage from Physical moves.
    - **Light Screen** reduces damage from Special moves.

    If the move is a critical hit (`crit == True`), screen effects are ignored.

    The reduction depends on the battle mode:
    - In single battles (`battle_mode != 2`) or if the trainer has only one active Pokémon 
      in a double battle, the screen reduces damage by 50% (multiplier = 0.5).
    - In double battles (`battle_mode == 2`) with multiple active Pokémon, the reduction is 
      approximately 33% (multiplier = 2/3).

    Args:
        trainer (Trainer): The defending trainer, whose field status is checked for Reflect or Light Screen.
        battle_mode (int): The current battle mode. Typically:
            - 1 for single battle
            - 2 for double battle
        move (Move): The move being used, which determines whether Reflect or Light Screen applies.
        crit (bool): Whether the move is a critical hit. Critical hits bypass screen effects.

    Returns:
        float: The multiplier to apply to the move's damage (1.0 if no screen effect applies, or if the move is a critical hit).
    """
    screen = 1
    if not crit and ((move.category == "Physical" and trainer.field['reflect'] > 0) or
                     (move.category == "Special" and trainer.field['lightscreen'] > 0)):

        if battle_mode != 2 or (battle_mode == 2 and
                                len(trainer.active_pokemon) == 1):
            screen = 0.5
        else:
            screen = 2/3

    return screen


def weather_mul(move: Move, weather: str) -> float:
    weather_mul = 1
    if weather == 'Sunny':
        if move.type == 'Fire':
            weather_mul = 1.5
        elif move.type == 'Water':
            weather_mul = 0.5
    if weather == 'Rainy':
        if move.type == 'Fire':
            weather_mul = 0.5
        elif move.type == 'Weater':
            weather_mul = 1.5
    if move.move_name == 'SolarBeam' and weather != 'Sunny':
        weather_mul = 0.5
    return weather_mul
