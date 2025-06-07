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
    def __init__(self,species_name,type1,type2,level,ability,move_list,held_item=None,effort_values=None,individual_values=None,base_stats=None,nature='Hardy',stats=None):
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
            ability (Abiltiy object): The Pokémon's ability.
            held_item (Held_Item object): The item held by the Pokémon.
            move_list (list): List of move objects the Pokémon can use.
        """
        self.species_name=species_name
        self.active1=False
        self.active2=False
        self.active=[self.active1,self.active2]
        self.type1=type1
        self.type2=type2
        self.type=[self.type1,self.type2]
        self.level=level
        self.effort_values=effort_values if effort_values else {'atk':0,'def':0,'spatk':0,'spdef':0,'spd':0}
        self.individual_values= individual_values if individual_values else {'atk':0,'def':0,'spatk':0,'spdef':0,'spd':0}
        self.base_stats=base_stats
        self.nature = nature
        if base_stats:
            self.stats = {
            "hp": ((2 * base_stats["hp"] + self.individual_values["hp"] +self.effort_values["hp"] // 4) * level) // 100 + level + 10,
            "atk": ((2 * base_stats["atk"] + self.individual_values["atk"] +self.effort_values["atk"] // 4) * level) // 100 + 5,
            "def": ((2 * base_stats["def"] + self.individual_values["def"] + self.effort_values["def"] // 4) * level) // 100 + 5,
            "spatk": ((2 * base_stats["spatk"] + self.individual_values["spatk"] + self.effort_values["spatk"] // 4) * level) // 100 + 5,
            "spdef": ((2 * base_stats["spdef"] + self.individual_values["spdef"] + self.effort_values["spdef"] // 4) * level) // 100 + 5,
            "spd": ((2 * base_stats["spd"] + self.individual_values["spd"] + self.effort_values["spd"] // 4) * level) // 100 + 5
            }
            # placeholder: code to use natures.json to buff and nerf stats
        else:
            self.stats = stats if stats else {'atk':0,'def':0,'spatk':0,'spdef':0,'spd':0}
        self.statchanges={'atk':0,'def':0,'spatk':0,'spdef':0,'spd':0,'evs':0,'acc':0}
        self.ability = ability #Ability object
        self.held_item = held_item #Held_Item object
        self.status={'psn':False,'brn':False,'prlz':False,'slp':0,'frz':0,'bdpsn':0}
        self.secondary_status={
        "Flinch": False,
        "Confused": 0,
        "Attracted": False,
        "Leech Seeded": [False,0], # Integer refers to which side of enemy gets the health regen in case of double battle
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

    @property
    def fainted(self):
        """Check if the Pokémon has fainted.

        Returns:
            bool: True if the Pokémon's current HP is 0, False otherwise.
        """
        return False if self.current_hp else True








