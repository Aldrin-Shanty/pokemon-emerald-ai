class Battle:
    def __init__(self, player1, player2):
        self.battle_turn = 0
        self.trainer_1 = player1
        self.trainer_2 = player2
        self.weather = 0
        # none = 0, sun = 1, rain = 2, sand = 3, hail = 3
        self.battle_mode = 1
        # single = 1, doubles = 2

    def turn_order(self):
        if self.battle_mode == 1:
            if self.trainer_1.pokemon_list[]

    def dmg_calc(self):
        pass

    def turn_effects(self):
        pass

    def battle(self):
        pass

class Trainer:
    def __init__(self,usable_items,pokemon_list):
        self.pokemon_list = pokemon_list
        self.active_pokemon_1=pokemon_list[0]
        self.active_pokemon_2=pokemon_list[1]
        self.usable_items=usable_items
        self.spikes=0
        self.reflect=0 # turns left
        self.lightscreen=0 # turns left
        self.protected=False
        self.leech_seeded=False
        self.foresighted=False
        self.helping_handed=False
        self.switching_out=False

    def switch_pokemon_1(self,active_pokemon_1,switching_pokemon_1):
        self.pokemon_list
        pass

    def switch_pokemon_2(self,active_pokemon_2,switching_pokemon_2):
        self.active_pokemon_2=active_pokemon
        pass

    def attack(self,active_pokemon,enemy_pokemon,move_slot):
        pass

    def use_item(self,active_pokemon,item):
        pass

class Pokemon:
    def __init__(self,species_id,type1,type2,level,effort_values,individual_values,base_stats,stats,nature,ability,held_item,move_list):
        self.species_id=species_id
        self.active_pokemon_1 = False
        self.active_pokemon_2 = False
        self.type1=type1
        self.type2=type2
        self.level=level
        self.effort_values=effort_values
        self.individual_values=individual_values
        self.base_stats=base_stats
        self.stats=stats
        self.nature = nature
        self.ability = ability
        self.held_item = held_item
        self.status=0
        # 0 - Healthy
        # 1 - Burn
        # 2 - Sleep
        # 3 - Poisoned
        # 4 - Badly Poisoned
        # 5 - Frozen
        # 6 - Paralyzed
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


