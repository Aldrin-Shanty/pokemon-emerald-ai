from Held_Item import HeldItem
from Abilities import Ability
from Move import Move


class Pokemon:
    def __init__(self, species_name: str, type1: str, type2: str, level: int, ability: Ability,
                 move_list: list[Move], held_item: HeldItem = None, effort_values: dict[str, int] = None,
                 individual_values: dict[str, int] = None, base_stats: dict[str, int] = None,
                 nature: str = 'Hardy', stats: dict[str, int] = None, friendship: int = 255) -> None:

        self.species_name = species_name
        self.active1 = False
        self.active2 = False
        self.active = [self.active1, self.active2]
        self.type1 = type1
        self.type2 = type2
        self.type = [self.type1, self.type2]
        self.level = level
        self.friendship = friendship

        self.effort_values = effort_values \
            if effort_values \
            else {'atk': 0, 'def': 0, 'spatk': 0, 'spdef': 0, 'spd': 0}

        self.individual_values = individual_values \
            if individual_values \
            else {'atk': 0, 'def': 0, 'spatk': 0, 'spdef': 0, 'spd': 0}

        self.nature = nature
        self.base_stats = base_stats

        if base_stats and individual_values and effort_values:

            self.stats = {
                "hp": ((2 * self.base_stats["hp"] + self.individual_values["hp"] + self.effort_values["hp"] // 4) * self.level)
                // 100 + level + 10,
                "atk": ((2 * self.base_stats["atk"] + self.individual_values["atk"] + self.effort_values["atk"] // 4) * self.level)
                // 100 + 5,
                "def": ((2 * self.base_stats["def"] + self.individual_values["def"] + self.effort_values["def"] // 4) * self.level)
                // 100 + 5,
                "spatk": ((2 * self.base_stats["spatk"] + self.individual_values["spatk"] + self.effort_values["spatk"] // 4) * self.level)
                // 100 + 5,
                "spdef": ((2 * self.base_stats["spdef"] + self.individual_values["spdef"] + self.effort_values["spdef"] // 4) * self.level)
                // 100 + 5,
                "spd": ((2 * self.base_stats["spd"] + self.individual_values["spd"] + self.effort_values["spd"] // 4) * self.level)
                // 100 + 5
            }
            # placeholder: code to use natures.json to buff and nerf stats
        else:
            self.stats = stats

        self.statchanges = {'atk': 0, 'def': 0, 'spatk': 0,
                            'spdef': 0, 'spd': 0, 'evs': 0, 'acc': 0}
        self.ability = ability  # Ability object
        self.held_item = held_item  # Held_Item object
        self.status = {'psn': False, 'brn': False,
                       'prlz': False, 'slp': 0, 'frz': 0, 'bdpsn': 0}

        self.secondary_status = {
            "Flinch": False,
            "Confused": 0,
            "Attracted": False,
            # Integer refers to which side of enemy gets the health regen in case of double battle
            "Leech Seeded": [False, 0],
            "Trapped": False,
            "Partially Trapped": 0,
            "Taunted": False,
            "Tormented": False,
            "Encore": 0,
            "Disabled": 0,
            "Yawn": 0,
            "Ingrained": False,
            "Charging Turn": False,
            "Recharging Turn": False,
            "Bide": 0,
            "Focus Energy": False,
            "Rage Lock": 0,
            "Destiny Bond": False,
            "Grudge": False,
            "Perish Song": 0,
            "Identified": False,
            "Minimized": False,
            "Substitute": False,
            "Stockpile": 0,
            "Helping Handed": False
        }

        self.current_hp = self.stats['hp']
        self.move_list = move_list

    @property
    def fainted(self) -> bool:
        return False if self.current_hp else True
