from math import floor

from Pokemon import Pokemon
from Usable_Item import UsableItem


class Trainer:

    def __init__(self,trainer_name: str,usable_items : list[UsableItem],pokemon_list : list[Pokemon]) -> None:

        self.trainer_name = trainer_name
        self.pokemon_list = pokemon_list # list of pokemon objects
        self.usable_items = usable_items # list of usable items

        self.field = {'Spikes':0,'Reflect':0,'Lightscreen':0,'Wish':[0,0],
                      'Future Sight': [{'attacker': None,'attacked_pos': 0,'turns': 0 },{'attacker': None,'attacked_pos': 0,'turns': 0 }],
                      'Doom Desire': [{'attacker': None,'attacked_pos': 0,'turns': 0 },{'attacker': None,'attacked_pos': 0,'turns': 0 }]}

        self.choice1 = {'switching':False,'attacking':False,'using_item':False}
        self.choice2 = {'switching':False,'attacking':False,'using_item':False}
        self.choices = [self.choice1,self.choice2]
        self.switching1 = None #pokemon object to switch to
        self.switching2 = None #pokemon object to switch to
        self.switchings = [self.switching1,self.switching2]
        self.using_item1 = None #Item object used
        self.using_item2 = None #Item object used
        self.using_items = [self.using_item1,self.using_item2]
        self.attacking1 = None #Move object
        self.attacking2 = None #Move object
        self.attackings = [self.attacking1,self.attacking2]

    @property
    def is_defeated(self) -> bool:

        no_of_defeated = 0

        for pokemon in self.pokemon_list:

            if pokemon.fainted:
                no_of_defeated += 1

        return True if no_of_defeated == 6 else False

    @property
    def active_pokemon(self) -> list[Pokemon]:

        active_pokemon_1 = [pokemon for pokemon in self.pokemon_list if pokemon.active[0]]
        active_pokemon_2 = [pokemon for pokemon in self.pokemon_list if pokemon.active[1]]
        return active_pokemon_1 + active_pokemon_2

    @staticmethod
    def use_heal_item(pokemon: Pokemon, item: UsableItem) -> bool:

        if pokemon.current_hp != pokemon.stats['hp']:
            heal_amnt = item.heal \
                if pokemon.stats['hp'] - pokemon.current_hp > item.heal \
                else pokemon.stats['hp'] - pokemon.current_hp

            pokemon.current_hp += heal_amnt
            print(f'{pokemon.species_name} has healed for {heal_amnt} points')
        else:
            print(f'{pokemon.species_name} is already healthy. It cant be healed')

        if not item.status_cure:
            item.quantity -= 1
            return True

        return False

    @staticmethod
    def use_percent_heal_item(pokemon: Pokemon, item: UsableItem) -> bool:

        if pokemon.current_hp != pokemon.stats['hp']:

            heal_amnt = floor(pokemon.stats['hp'] * item.percent_heal / 100) \
                if pokemon.stats['hp'] - pokemon.current_hp > floor(pokemon.stats['hp'] * item.percent_heal / 100) \
                else pokemon.stats['hp'] - pokemon.current_hp

            pokemon.current_hp += heal_amnt
            print(f'{pokemon.species_name} has healed for {heal_amnt} points')
        else:
            print(f'{pokemon.species_name} is already healthy, cant be healed further')

        if not item.status_cure:
            item.quantity -= 1
            return True

        return False

    @staticmethod
    def use_all_pp_item(pokemon: Pokemon, item: UsableItem) -> bool:

        pp_needed_moves = []

        for move in pokemon.move_list:

            if move.power_points != move.max_power_points:
                pp_needed_moves.append(move)

        if len(pp_needed_moves) == 0:
            print(f'All moves have full pp, {item.item_name} can\'t be used')
            return False

        for move in pp_needed_moves:
            used_pp = move.max_power_points - move.power_points
            move.power_points += item.pp if used_pp > item.pp else used_pp
            print(f'{move.move_name}\'s power points have been replenished to '
                  f'({move.power_points}/{move.max_power_points})')

        item.quantity -= 1
        return True

    @staticmethod
    def use_pp_item(pokemon: Pokemon, item: UsableItem) -> bool:

        for move in pokemon.move_list:
            print(f'{move.move_name}({move.power_points}/{move.max_power_points})', end='\t')

        selected_move_index = int(input('Which move\'s powerpoint to increase(1-4) : '))
        selected_move = pokemon.move_list[selected_move_index]
        used_pp = selected_move.max_power_points - selected_move.power_points

        if used_pp > 0:
            selected_move.power_points += item.pp if used_pp > item.pp else used_pp
            print(f'{selected_move.move_name}\'s power points have been replenished to '
                  f'({selected_move.power_points}/{selected_move.max_power_points})')
            item.quantity -= 1
            return True
        else:
            print(f'{selected_move.move_name} has {selected_move.power_points}/{selected_move.max_power_points}'
                  f', {item.item_name} can\'t be used')
            return False

    @staticmethod
    def use_status_cure_item(pokemon: Pokemon, item: UsableItem) -> bool:

        for status,turn in pokemon.status:

            if status == item.status_cure or item.status_cure == 'all':

                pokemon.status[status] = 0 if type(turn) == int else False
                print(f'{pokemon.species_name}\'s {pokemon.status} status has been cured')
                item.quantity -= 1
                return True
        else:
            print(f'{pokemon.species_name}\'s {pokemon.status} status cannot be cured using {item.item_name}')
            return False

    def use_item(self,item: UsableItem,pokemon: Pokemon) -> bool:

        is_item_used = False

        if not pokemon.fainted:

            if item.heal:
                is_item_used = self.use_heal_item(pokemon,item)

            if item.percent_heal:
                is_item_used = self.use_percent_heal_item(pokemon,item)

            if item.pp:
                is_item_used = self.use_pp_item(pokemon,item)

            if item.pp_all:
                is_item_used = self.use_all_pp_item(pokemon,item)

            if item.status_cure:
                is_item_used = self.use_status_cure_item(pokemon,item)
            else:
                print(f'{item.item_name} cannot be used on a pokemon')
                is_item_used = False

        else:
            print(f'{pokemon.species_name} has fainted, {item.item_name} cant\'t be used')
            is_item_used = False

        if item.quantity == 0:
            self.usable_items.remove(item)

        return is_item_used

    def switch_pokemon(self,switch_pokemon: Pokemon,sent_pokemon: Pokemon) -> None:

        #placeholder: for things that will modify stuff when pokemon switched out
        if sent_pokemon.status['bdpsn'] > 1:
            sent_pokemon.status['bdpsn'] = 1

        for stat in switch_pokemon.statchanges:
            switch_pokemon.statchanges[stat] = 0

        switch_pokemon.active[self.active_pokemon.index(switch_pokemon)] = False
        sent_pokemon.active[self.active_pokemon.index(sent_pokemon)] = True
        self.active_pokemon[self.active_pokemon.index(switch_pokemon)] = sent_pokemon
