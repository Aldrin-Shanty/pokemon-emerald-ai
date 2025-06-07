class Pokemon:
    """A class to represent a Pokémon with its attributes and battle-related properties.

    Attributes:
        species_name (str): The name of the Pokémon species.
        active (list): List indicating if the Pokémon is active in battle positions [False, False].
        type (list): List of the Pokémon's types [type1, type2].
        level (int): The Pokémon's level.
        effort_values (dict): Dictionary of effort values (EV) for each stat.
        individual_values (dict): Dictionary of individual values (IV) for each stat.
        base_stats (dict): Dictionary of base stats for the Pokémon.
        stats (dict): Calculated stats based on base stats, EVs, IVs, and level.
        nature (str): The Pokémon's nature, affecting stat growth.
        ability (str): The Pokémon's ability.
        held_item (str): The item held by the Pokémon.
        status (dict): Dictionary tracking primary status conditions (e.g., poison, burn).
        secondary_status (dict): Dictionary tracking secondary status conditions (e.g., flinch, confused).
        current_hp (int): The Pokémon's current hit points.
        move_list (list): List of moves the Pokémon can use.
    """
    def __init__(self,species_name,type1,type2,level,effort_values,individual_values,base_stats,nature,ability,held_item,move_list):
        """Initialize a new Pokémon instance.

        Args:
            species_name (str): The name of the Pokémon species.
            type1 (str): The Pokémon's primary type.
            type2 (str): The Pokémon's secondary type (None if monotype).
            level (int): The Pokémon's level.
            effort_values (dict): Dictionary of effort values for each stat.
            individual_values (dict): Dictionary of individual values for each stat.
            base_stats (dict): Dictionary of base stats for the Pokémon.
            nature (str): The Pokémon's nature.
            ability (str): The Pokémon's ability.
            held_item (str): The item held by the Pokémon.
            move_list (list): List of move objects the Pokémon can use.
        """
        self.species_name=species_name
        self.active = [False,False]
        self.type=[type1,type2]
        self.level=level
        self.effort_values=effort_values
        self.individual_values=individual_values
        self.base_stats=base_stats
        self.stats = {
        "hp": ((2 * base_stats["hp"] + individual_values["hp"] + effort_values["hp"] // 4) * level) // 100 + level + 10,
        "atk": ((2 * base_stats["atk"] + individual_values["atk"] + effort_values["atk"] // 4) * level) // 100 + 5,
        "def": ((2 * base_stats["def"] + individual_values["def"] + effort_values["def"] // 4) * level) // 100 + 5,
        "spatk": ((2 * base_stats["spatk"] + individual_values["spatk"] + effort_values["spatk"] // 4) * level) // 100 + 5,
        "spdef": ((2 * base_stats["spdef"] + individual_values["spdef"] + effort_values["spdef"] // 4) * level) // 100 + 5,
        "spd": ((2 * base_stats["spd"] + individual_values["spd"] + effort_values["spd"] // 4) * level) // 100 + 5
        }
        self.nature = nature
        self.ability = ability
        self.held_item = held_item
        self.status={'psn':False,'brn':False,'prlz':False,'slp':0,'frz':0,'bdpsn':0}
        self.secondary_status={
        "Flinch": False,
        "Confused": 0,
        "Attracted": False,
        "Leech Seeded": [False,0], # Integer refers to which side of enemy gets the health regenf
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
        "Substitute": False
        }
        self.current_hp=self.stats['hp']
        self.move_list=move_list
        self.selected_move=None

    @property
    def fainted(self):
        """Check if the Pokémon has fainted.

        Returns:
            bool: True if the Pokémon's current HP is 0, False otherwise.
        """
        return False if self.current_hp else True








