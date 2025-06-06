# import random

class Battle:
    def __init__(self, player1, player2):
        self.battle_turn = 0
        self.trainers = [player1,player2]
        self.weather = {'sunny':0,'rainy':0,'hail': 0,'sandstorm': 0}
        self.battle_mode = 1
    @property
    def turn_order(self):
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
        pass

    def turn_effects(self):
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



        # this function going to do all the wierd cases for each ability moves later...
        pass

class Trainer:
    def __init__(self,trainer_name,usable_items,pokemon_list):
        self.trainer_name=trainer_name
        self.pokemon_list = pokemon_list
        self.usable_items=usable_items
        self.field={'spikes':0,'reflect':0,'lightscreen':0,'trap_turns':0}
        self.switching_out=[False,False]
        self.using_item=[None,None] # None implies not using item, else item object placed
        self.attacking=[None,None] # None implies not attack,else move object placed
        self.attacking_who=0 # 0 implies no one, 1 - first active pokemon, 2 - second active pokemon

    @property
    def is_defeated(self):
        no_of_defeated=0
        for pokemon in self.pokemon_list:
            if pokemon.fainted:
                no_of_defeated+=1
        return True if no_of_defeated==6 else False
    @property
    def active_pokemon(self):
        return [pokemon for pokemon in self.pokemon_list if pokemon.active[0]]+[pokemon for pokemon in self.pokemon_list if pokemon.active[1]]

    def switch_pokemon(self,pokemon_index,switch_pos=1):
        # switch pos :-  switching pokemon in position 1 -> 1 , switching pokemon in position 2 -> 2
        self.active_pokemon[switch_pos-1]= self.pokemon_list[pokemon_index]
        self.switching_out[switch_pos-1]=True
        self.active_pokemon[switch_pos-1].status['bdpsn']=1

    def attack(self,move_slot,user_pos=1,enemy_pos=1):
        move_used=self.active_pokemon[user_pos-1].move_list[move_slot]
        self.attacking_who=enemy_pos
        self.attacking[user_pos]= move_used
        return move_used

    def use_item(self,item_key,use_pos=1):
        #use_pos refers to index in pokemon_list not in active_pokemon
        item=self.usable_items[item_key]
        pokemon=self.pokemon_list[use_pos]
        pokemon.current_hp+=item.heal_amount
        self.usable_items[item]-=1
        #not completed need to develop idea more

class Pokemon():
    def __init__(self,species_id,type1,type2,level,effort_values,individual_values,base_stats,stats,nature,ability,held_item,move_list):
        self.species_id=species_id
        self.active = [False,False]
        self.type=[type1,type2]
        self.level=level
        self.effort_values=effort_values
        self.individual_values=individual_values
        self.base_stats=base_stats
        self.stats=stats
        self.nature = nature
        self.ability = ability
        self.held_item = held_item
        self.status={'psn':False,'brn':False,'prlz':False,'slp':0,'frz':0,'bdpsn':0}
        self.secondary_status=0
        # 0  - None
        # 1  - Flinch
        # 2  - Confused
        # 3  - Attracted
        # 4  - Leech Seeded
        # 5  - Nightmare
        # 6  - Trapped
        # 7  - Partially Trapped
        # 8  - Taunted
        # 9  - Tormented
        # 10 - Encore
        # 11 - Disabled
        # 12 - Yawn (Drowsy)
        # 13 - Ingrained
        # 14 - Charging Turn
        # 15 - Recharging Turn
        # 16 - Bide
        # 17 - Focus Energy
        # 18 - Rage Lock
        # 19 - Destiny Bond
        # 20 - Grudge
        # 21 - Perish Song
        # 22 - Identified
        # 23 - Minimized
        # 24 - Substitute
        self.current_hp=self.stats['hp']
        self.max_hp=self.stats['hp']
        self.move_list=move_list
    @property
    def fainted(self):
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
        self.target=target # single(1),double(2),all(3)

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


