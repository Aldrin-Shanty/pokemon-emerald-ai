# import random

class Battle:
    """A class to manage a Pokémon battle between two trainers.

    Attributes:
        battle_turn (int): The current turn number of the battle.
        trainers (list): List of two trainer objects participating in the battle.
        weather (dict): Dictionary tracking weather effects and their durations.
        battle_mode (int): The mode of the battle (1 for singles, 2 for doubles).
    """
    def __init__(self, player1, player2):
        """Initialize a new Battle instance.

        Args:
            player1: First trainer object participating in the battle.
            player2: Second trainer object participating in the battle.
        """
        self.battle_turn = 0
        self.trainers = [player1,player2]
        self.weather = {'sunny':0,'rainy':0,'hail': 0,'sandstorm': 0}
        self.battle_mode = 1
    @property
    def turn_order(self):
        """Determine the turn order of Pokémon based on their speed and action priorities.

        Returns:
            list: Ordered list of Pokémon based on calculated priorities.
        """
        priority=[[0] * self.battle_mode] * len(self.trainers)
        for trainer in self.trainers:
            for active in range(self.battle_mode):
                if self.trainers[trainer].switching_out[active]:
                    priority[trainer][active]+=40
                if self.trainers[trainer].using_item[active]:
                    priority[trainer][active] += 30
        pokemons=[[pokemon for pokemon in trainer.active_pokemon] for trainer in self.trainers]
        pokemons_temp=pokemons.copy()
        pokemons_temp=[pokemon for trainer in pokemons_temp for pokemon in trainer]
        pokemons_temp.sort(key=lambda pokemon: pokemon.stats['spd'])
        for i,trainer in enumerate(pokemons):
            for j,pokemon in enumerate(trainer):
                if pokemon.selected_move is not None:
                    priority[i][j]+=pokemon.selected_move.priority
                priority[i][j]+= pokemons_temp.index(pokemon)/(len(pokemons_temp)-1)
        order=dict(zip([pokemon for trainer in pokemons for pokemon in trainer], [active_prio for trainer in priority for active_prio in trainer ]))
        order = sorted(order, key=order.get, reverse=True)
        return order

    def dmg_calc(self):
        """Calculate damage for moves used in the battle.

        Note:
            This method is currently a placeholder and needs implementation.
        """
        pass

    def turn_effects(self):
        """Apply turn-based effects such as weather, status conditions, and field effects.

        Updates the state of weather, trainer fields, and Pokémon statuses.
        """
        order=self.turn_order
        for weather,turns in self.weather:
            turns-=1 if turns>0 else 0
        for trainer in self.trainers:
            trainer.switching_out=[False,False]
            trainer.field['reflect']-=1 if trainer.field['reflect'] else 0
            trainer.field['lightscreen']-=1 if trainer.field['lightscreen'] else 0
            trainer.field['trap_turns']-=1 if trainer.field['trap_turns'] else 0
        for pokemon in order:
            pokemon.current_hp-=(pokemon.status['hp']/16 if pokemon.current_hp > 0 else 0) if (pokemon.status['psn'] or pokemon.status['brn']) else pokemon.current_hp
            pokemon.current_hp-=(pokemon.status['hp']*(pokemon.status['bdpsn']+1)/16 if pokemon.current_hp > 0 else 0) if (pokemon.status['bdpsn']) else pokemon.current_hp
            pokemon.status['bdpsn']+=1
            pokemon.status['slp']-=1 if pokemon.status['slp'] else 0
            pokemon.status['frz'] -= 1 if pokemon.status['frz'] else 0

    def battle(self):
        """Manage the main battle loop, handling turn progression and player choices.

        Prints battle status and prompts for player actions such as moves, switches, or item usage.
        Continues until one trainer is defeated.
        """
        print(f'{self.trainers[0].trainer_name} vs {self.trainers[1].name} begins...')
        for trainer in self.trainers:
            trainer.active_pokemon[0]=trainer.pokemon_list[0]
            if self.battle_mode==2:
                trainer.active_pokemon[1]=trainer.pokemon_list[1]
                print(f'{trainer.trainer_name} sents out {trainer.active_pokemon[0]} and {trainer.active_pokemon[1]}!')
            else:
                print(f'{trainer.trainer_name} sents out {trainer.active_pokemon[0]}!')
        while not self.trainers[0].is_defeated or not self.trainers[1].is_defeated:
            if self.weather['sunny']:
                print('The sunlight is strong')
            elif self.weather['rainy']:
                print('It is raining')
            elif self.weather['hail']:
                print('Hail continues to fall')
            elif self.weather['sandstorm']:
                print('The sandstorm is raging')
            self.battle_turn += 1
            print('Battle Turn: ', self.battle_turn)
            order = self.turn_order
            for pokemon in order:
                moves = pokemon.move_list
                switch=None
                items=None
                for trainer in self.trainers:
                    if pokemon in trainer.active_pokemon:
                        switch=trainer.pokemon_list.copy().remove(pokemon)
                        if self.battle_mode==2:
                            switch=switch.remove(trainer.active_pokemon.copy().remove(pokemon)[0])
                        items=trainer.usable_items
                choices=[moves,switch,items,'forfeit']
                print(f'Choose the move(m1-m4):')
                for move in moves:
                    print(f'{move.move_name}',end='\t')
                print(f'Switch Pokemon(p1-p6):')
                for pokemon_switchable in switch:
                    print(f'{pokemon_switchable.species_name}(lv:{pokemon_switchable.level})',end='   ')
                print(f'Items')
class Trainer:
    """A class to represent a Pokémon trainer and their actions in a battle.

    Attributes:
        trainer_name (str): The name of the trainer.
        pokemon_list (list): List of Pokémon owned by the trainer.
        usable_items (dict): Dictionary of items the trainer can use, with quantities.
        field (dict): Dictionary tracking field effects like spikes, reflect, etc.
        switching_out (list): List indicating if Pokémon in active positions are switching out.
        using_item (list): List indicating items being used for each active Pokémon position.
        attacking (list): List of moves being used by Pokémon in active positions.
        attacking_who (int): Indicates target of attack (0 for none, 1 for first enemy, 2 for second enemy).
    """
    def __init__(self,trainer_name,usable_items,pokemon_list):
        """Initialize a new Trainer instance.

        Args:
            trainer_name (str): The name of the trainer.
            usable_items (dict): Dictionary of usable items with their quantities.
            pokemon_list (list): List of Pokémon objects owned by the trainer.
        """
        self.trainer_name=trainer_name
        self.pokemon_list = pokemon_list
        self.usable_items=usable_items
        self.field={'spikes':0,'reflect':0,'lightscreen':0,'trap_turns':0}
        self.switching_out=[False,False]
        self.using_item=[None,None]
        self.attacking=[None,None]
        self.attacking_who=0

    @property
    def is_defeated(self):
        """Check if the trainer is defeated based on Pokémon fainting.

        Returns:
            bool: True if all Pokémon in pokemon_list have fainted, False otherwise.
        """
        no_of_defeated=0
        for pokemon in self.pokemon_list:
            if pokemon.fainted:
                no_of_defeated+=1
        return True if no_of_defeated==6 else False

    @property
    def active_pokemon(self):
        """Get the list of currently active Pokémon.

        Returns:
            list: List of Pokémon objects that are currently active in battle.
        """
        return [pokemon for pokemon in self.pokemon_list if pokemon.active[0]]+[pokemon for pokemon in self.pokemon_list if pokemon.active[1]]

    def switch_pokemon(self,pokemon_index,switch_pos=1):
        """Switch an active Pokémon with another from the trainer's Pokémon list.

        Args:
            pokemon_index (int): Index of the Pokémon in pokemon_list to switch in.
            switch_pos (int, optional): Position (1 or 2) of the active Pokémon to replace. Defaults to 1.
        """
        self.active_pokemon[switch_pos-1]= self.pokemon_list[pokemon_index]
        self.switching_out[switch_pos-1]=True
        self.active_pokemon[switch_pos-1].status['bdpsn']=1

    def attack(self,move_slot,user_pos=1,enemy_pos=1):
        """Execute an attack using a move from an active Pokémon.

        Args:
            move_slot (int): Index of the move in the Pokémon's move_list to use.
            user_pos (int, optional): Position (1 or 2) of the attacking Pokémon. Defaults to 1.
            enemy_pos (int, optional): Position (1 or 2) of the target enemy Pokémon. Defaults to 1.

        Returns:
            object: The move object used in the attack.
        """
        move_used=self.active_pokemon[user_pos-1].move_list[move_slot]
        self.attacking_who=enemy_pos
        self.attacking[user_pos]= move_used
        return move_used

    def use_item(self,item_key,use_pos=1):
        """Use an item on a specified Pokémon.

        Args:
            item_key: Key identifying the item in usable_items dictionary.
            use_pos (int, optional): Index in pokemon_list of the Pokémon to apply the item to. Defaults to 1.

        Note:
            This method is incomplete and requires further development.
        """
        item=self.usable_items[item_key]
        pokemon=self.pokemon_list[use_pos]
        pokemon.current_hp+=item.heal_amount
        self.usable_items[item]-=1
        #not completed need to develop idea more

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
        "Leech Seeded": False,
        "Nightmare": False,
        "Trapped": False,
        "Partially Trapped": 0,
        "Taunted": False,
        "Tormented": False,
        "Encore": False,
        "Disabled": 0,
        "Yawn": False,
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
class Move:
    def __init__(self,move_name,base_power,power_points,type_of_move,accuracy_of_move, category_of_move, has_contact,user_stat_change,enemy_stat_change,target = 1,recoil=0,priority = 0,no_of_hits=1,crit_chance=0.0625,):
        self.move_name=move_name
        self.base_power=base_power
        self.power_points=power_points
        self.type=type_of_move
        self.no_of_hits=no_of_hits
        self.crit_chance=crit_chance
        self.accuracy=accuracy_of_move
        self.category=category_of_move
        self.has_contact=has_contact
        self.priority=priority
        self.recoil = recoil
        self.user_stat_change=user_stat_change
        self.enemy_stat_change=enemy_stat_change
        self.target=target

class Ability:
    def __init__(self,ability_id):
        self.ability_id=ability_id

class HeldItem:
    def __init__(self,item_id,dmg_multiplier,health_restore):
        self.item_id=item_id
        self.dmg_multiplier=dmg_multiplier
        self.health_restore=health_restore

class UsableItem:
    def __init__(self,item_id,heal_amount,status_cure,pp_restore):
        self.item_name=item_id
        self.heal_amount=heal_amount
        self.status_cure=status_cure
        self.pp_restore=pp_restore


