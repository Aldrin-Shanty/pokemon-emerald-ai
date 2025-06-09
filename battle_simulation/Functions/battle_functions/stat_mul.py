import json
from pathlib import Path
from typing import List

from battle_simulation.Class.Move import Move
from battle_simulation.Class.Pokemon import Pokemon
from battle_simulation.Class.Trainer import Trainer


project_root = Path(__file__).resolve().parent.parent.parent

type_chart_path = project_root / 'data' / 'type_chart.json'


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
    if move.name == 'SolarBeam' and weather != 'Sunny':
        weather_mul = 0.5
    return weather_mul


def targets_mul(battle_mode: int, targets: int, trainer: Trainer) -> float:
    target = 1
    if battle_mode == 2:
        if targets == 1:
            target = 1
        else:
            if len(trainer.active_pokemon) > 1:
                target = 0.5
    return target


def stab_mul(move_type: str, pokemon_type: List[str]) -> float:
    stab = 1
    if move_type in pokemon_type:
        stab = 1.5
    return stab


def burn_mul(pokemon:Pokemon, move_category: str) -> float:
    burn = 1
    if (pokemon.status['brn'] and
        pokemon.ability != "guts" and
            move_category == "Physical"):
        burn = 0.5
    return burn


def crit_mul(ability: str, move: str, crit: bool) -> int:
    crit_mul = 1
    crit_ignore_abilities = ["Battle Armor", "Sheel Armor"]
    crit_ignore_moves = ["Doom Desire", "Future Sight", "Spit Up"]
    if crit and move not in crit_ignore_moves and ability not in crit_ignore_abilities:
        crit_mul = 2
    return crit_mul


def type_mul(attack_type: str, defend_type: str, move: str) -> float:

    type_negate = ["Struggle", "Future Sight", "Beat Up", "Doom Desire"]
    type_mul = 1

    if move in type_negate:
        return type_mul

    type_chart = None
    with open('type_chart_path', 'r') as file:
        type_chart = json.load(file)

    type_mul = type_chart[attack_type][defend_type]
    return type_mul




