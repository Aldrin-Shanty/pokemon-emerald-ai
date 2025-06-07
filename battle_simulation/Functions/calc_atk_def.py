import random
from math import ceil

from battle_simulation.Class.Move import Move
from battle_simulation.Class.Pokemon import Pokemon


def calc_stage_mul(change: int) -> float:
    """Calculates the multiplier corresponding to a stat stage change.

    In the Pokémon stat stage system:
    - Positive stage changes increase the stat via (2 + stage) / 2.
    - Negative stage changes decrease the stat via 2 / (2 + stage).

    Args:
        change (int): The stage change value, typically ranging from -6 to +6.

    Returns:
        float: The corresponding multiplier to apply to the base stat.
    """

    mul = 0
    if change < 0:
        mul = 2/(2+change)
    else:
        mul = (2+change)/2
    return mul


def calc_atk_def(dealing_pokemon: Pokemon, taking_pokemon: Pokemon,
                 move: Move) -> list[int]:
    """Calculates the effective attack and defense stats for a move, factoring in stat changes and critical hits.

    This function computes the effective attack and defense values to be used when `dealing_pokemon` uses `move` 
    against `taking_pokemon`. It accounts for stat stage changes and whether the move results in a critical hit,
    which can ignore certain stat modifiers. The calculation uses a stage multiplier function `calc_stage_mul`.

    The function supports both Physical and Special moves:
    - Physical moves use the `atk` and `def` stats.
    - Special moves use the `spatk` and `spdef` stats.

    Args:
        dealing_pokemon (Pokemon): The Pokémon using the move. Its stats and stat stage changes determine the attack value.
        taking_pokemon (Pokemon): The Pokémon targeted by the move. Its stats and stat stage changes determine the defense value.
        move (Move): The move being used. Determines whether the attack is Physical or Special, and specifies the critical hit chance.

    Returns:
        list[int]: A list containing two integers:
            - The effective attack value (after applying stat stage multipliers or critical hit logic).
            - The effective defense value (after applying stat stage multipliers or critical hit logic).

    Notes:
        - A critical hit bypasses negative attack stage changes for the attacker and positive defense stage changes for the defender.
        - Stage multipliers are applied via the `calc_stage_mul` function.
        - The returned values are rounded up using `ceil`.
    """

    crit = random.choices(population=[False, True],
                          weights=[(1-move.crit_chance),
                          move.crit_chance])

    atk = 0
    defence = 0
    atk_var = 'atk' if move.category == "Physical" else 'spatk'
    def_var = 'def' if move.category == "Physical" else 'spdef'

    atk = dealing_pokemon.stats[atk_var]
    if dealing_pokemon.statchanges[atk_var] < 0 and crit:
        atk = dealing_pokemon.stats[atk_var]
    else:
        atk *= calc_stage_mul(dealing_pokemon.statchanges[atk_var])

    if taking_pokemon.statchanges[def_var] > 0 and crit:
        defence = taking_pokemon.stats[def_var]
    else:
        defence *= calc_stage_mul(taking_pokemon.statchanges[def_var])

    return [ceil(atk), ceil(defence)]
