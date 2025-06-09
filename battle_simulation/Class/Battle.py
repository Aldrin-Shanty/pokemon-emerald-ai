import random

from Trainer import Trainer
from Pokemon import Pokemon
from Move import Move
from battle_simulation.Functions.battle_functions.calc_atk_def import calc_atk_def
from battle_simulation.Functions.battle_functions.stat_mul import screen_calc
from battle_simulation.Functions.battle_functions.stat_mul import weather_mul


class Battle:
    def __init__(self, player1: Trainer, player2: Trainer, weather: str = None, weather_turn: int = 0, battle_mode: int = 1) -> None:
        self.battle_turn = 0
        self.trainers = [player1, player2]
        self.weather = weather  # Rainy Sunny Hail Sandstorm or None
        self.weather_turn = weather_turn
        self.battle_mode = battle_mode  # 1- singles # 2- doubles

    def turn_order(self) -> list[Pokemon]:
        priority = {trainer: {pokemon: 0 for pokemon in trainer.active_pokemon}
                    for trainer in self.trainers}

        for trainer in self.trainers:

            for pokemon in trainer.active_pokemon:
                position = trainer.active_pokemon.index(pokemon)

                if trainer.choices[position]['switching']:

                    if self.trainers.index(trainer) == 2:
                        priority[trainer][pokemon] += 39
                    elif self.trainers.index(trainer) == 1:
                        priority[trainer][pokemon] += 40

                if trainer.choices[position]['using_item']:
                    priority[trainer][pokemon] += 30

                if trainer.choices[position]['attacking']:
                    move = trainer.attackings[position]
                    priority[trainer][pokemon] += move.priority

        priority = [[pokemon, priority[trainer][pokemon]]
                    for trainer in priority for pokemon in trainer.active_pokemon]

        priority.sort(
            key=lambda pokemon: pokemon[0].stats['spd'], reverse=True)
        speed = [x for x in range(len(priority)-1, -1, -1)]

        for i in range(len(priority)):
            priority[i][1] += speed[i]/len(priority)-1

        priority.sort(key=lambda pokemon: pokemon[1], reverse=True)
        priority = [prio[0] for prio in priority]
        return priority

    def dmg_calc(self, dmg_taken_pokemon: Pokemon, dmg_deal_pokemon: Pokemon, move: Move) -> int:
        """Calculate damage for moves used in the battle.

        Note:
            This method is currently a placeholder and needs implementation.
        """
        crit = random.choices(population=[False, True],
                              weights=[(1-move.crit_chance),
                                       move.crit_chance])[0]
        power = move.base_power

        atk, defence = calc_atk_def(
            dmg_deal_pokemon, dmg_taken_pokemon, move, crit)

        burn = 1
        if (dmg_deal_pokemon.status['brn'] and
            dmg_deal_pokemon.ability != "guts" and
                move.type == "Physical"):
            burn = 0.5

        screen = screen_calc(self.trainer_of_active_pokemon(dmg_taken_pokemon),
                             self.battle_mode, move, crit)

        weather = weather_mul(
            move, self.weather) if self.weather_turn != 0 else 1

        critical = 2 if crit else 1

        target = 1
        if self.battle_mode == 2:
            if move.no_of_targets == 1:
                target = 1
            else:
                trainer = self.trainer_of_active_pokemon(dmg_taken_pokemon)
                if len(trainer.active_pokemon) > 1:
                    target = 0.5

        level_based_dmg = (2*dmg_deal_pokemon.level/5)+2
        stat_based_damage = power*(atk/defence)/50
        status_eff_damage = burn * screen * target * weather

        damage = level_based_dmg * stat_based_damage * status_eff_damage * critical
        # placeholder have to complete these (FF+2)×Stockpile×critical×DoubleDmg×Charge×HH×STAB×Type1×Type2×random

        return 1

    def trainer_of_active_pokemon(self, pokemon: Pokemon) -> Trainer:
        owner = None

        for trainer in self.trainers:

            if pokemon in trainer.active_pokemon:
                owner = trainer

        return owner

    def weather_turn_effects(self, order) -> None:
        if self.weather == 'Sunny':

            if self.weather_turn > 1:
                print('The sunlight is strong')
            elif self.weather_turn == 1:
                print('The sunlight faded')

        elif self.weather == 'Rainy':

            if self.weather_turn > 1:
                print('It is raining')
            elif self.weather_turn == 1:
                print('The rain stopped')

        elif self.weather == 'Hail':

            if self.weather_turn > 1:
                print('Hail continues to fall')

                for pokemon in order:
                    types = ['Ice']
                    if pokemon.type[0] not in types and pokemon.type[1] not in types:
                        damage = pokemon.stats['hp'] // 16

                        pokemon.current_hp -= (damage if damage > 1 else 1) \
                            if pokemon.current_hp > damage \
                            else pokemon.current_hp

                        print(f"{self.trainer_of_active_pokemon(pokemon).trainer_name}'s {pokemon.species_name} "
                              f"was buffeted by hail")
            elif self.weather_turn == 1:
                print('The hail subsided')

        elif self.weather == 'Sandstorm':

            if self.weather_turn > 1:
                print('The sandstorm is raging')

                for pokemon in order:
                    types = ['Rock', 'Steel', 'Ground']
                    if pokemon.type[0] not in types and pokemon.type[1] not in types:
                        damage = pokemon.stats['hp'] // 16

                        pokemon.current_hp -= (damage if damage > 1 else 1) \
                            if pokemon.current_hp > damage \
                            else pokemon.current_hp

                        print(f"{self.trainer_of_active_pokemon(pokemon).trainer_name}'s {pokemon.species_name} "
                              f"was buffeted by sandstorm")
            elif self.weather_turn == 1:
                print('The sandstorm subsided')
        self.weather_turn -= 1

    def status_turn_effects(self, order) -> None:
        for pokemon in order:

            if pokemon.status['psn']:
                damage = pokemon.stats['hp'] // 16

                pokemon.current_hp -= (damage if damage > 1 else 1) \
                    if pokemon.current_hp > damage \
                    else pokemon.current_hp

                print(f"{self.trainer_of_active_pokemon(pokemon).trainer_name}'s "
                      f"{pokemon.species_name} was hurt by poison")
            elif pokemon.status['bdpsn']:
                damage = pokemon.stats['hp'] * \
                    (pokemon.status['bdpsn'] + 1) // 16

                pokemon.current_hp -= (damage if damage > 1 else 1) \
                    if pokemon.current_hp > damage \
                    else pokemon.current_hp

                print(f"{self.trainer_of_active_pokemon(pokemon).trainer_name}'s "
                      f"{pokemon.species_name} was hurt badly by poison")

                pokemon.status['bdpsn'] += 1
            elif pokemon.status['brn']:
                damage = pokemon.stats['hp'] // 16

                pokemon.current_hp -= (damage if damage > 1 else 1) \
                    if pokemon.current_hp > damage \
                    else pokemon.current_hp

                print(f"{self.trainer_of_active_pokemon(pokemon).trainer_name}'s "
                      f"{pokemon.species_name} was hurt by burn")
            elif pokemon.status['slp']:
                pokemon.status['slp'] -= 1
            elif pokemon.status['frz']:
                pokemon.status['frz'] -= 1

    def secondary_status_turn_effects(self, order) -> None:
        for pokemon in order:
            trainer = self.trainer_of_active_pokemon(pokemon)

            if pokemon.secondary_status['Leech Seeded'][0]:
                leech_dmg_ratio = pokemon.stats['hp'] // 8
                leech_seeded_trainer_pos = self.trainers.index(trainer)
                leech_seed_used_trainer = self.trainers[- (
                    leech_seeded_trainer_pos + 1)]
                leech_seed_used_trainer_pos = pokemon.secondary_status['Leech Seeded'][1]
                leech_seed_used_pokemon = leech_seed_used_trainer.active_pokemon[
                    leech_seed_used_trainer_pos]

                leech_dmg = (leech_dmg_ratio if leech_dmg_ratio > 1 else 1) \
                    if pokemon.current_hp > leech_dmg_ratio \
                    else pokemon.current_hp

                leech_seed_used_pokemon.stats['hp'] += leech_dmg
                pokemon.current_hp -= leech_dmg
                print(f"{trainer.trainer_name}'s {pokemon.species_name}'s health is sapped by"
                      f" {leech_seed_used_trainer.trainer_name}'s {leech_seed_used_pokemon.species_name}")

            if pokemon.secondary_status['Perish Song'] > 1:
                print(f"{trainer.trainer_name}'s {pokemon.species_name} perish count has fallen to"
                      f" {pokemon.secondary_status['Perish Song'] - 1}")
                pokemon.secondary_status['Perish Song'] -= 1
            elif pokemon.secondary_status['Perish Song'] == 1:
                pokemon.current_hp = 0
                pokemon.secondary_status['Perish Song'] -= 1

            if pokemon.secondary_status['Yawn'] > 1:
                pokemon.secondary_status['Yawn'] -= 1
            elif pokemon.secondary_status['Yawn'] == 1:
                pokemon.status['slp'] = random.randint(1, 4)
                print(
                    f"{trainer.trainer_name}'s {pokemon.species_name} has fallen asleep")
                pokemon.secondary_status['Yawn'] -= 1

            if pokemon.secondary_status['Partially Trapped'] > 1:
                damage = pokemon.stats['hp'] // 16

                pokemon.current_hp -= (damage if damage > 1 else 1) \
                    if pokemon.current_hp > damage \
                    else pokemon.current_hp

                print(
                    f"{trainer.trainer_name}'s {pokemon.species_name} is hurt by the traps")
                pokemon.secondary_status['Partially Trapped'] -= 1
            elif pokemon.secondary_status['Partially Trapped'] == 1:
                print(
                    f"{trainer.trainer_name}'s {pokemon.species_name} was freed from the traps")
                pokemon.secondary_status['Partially Trapped'] -= 1

    def tertiary_status_turn_effects(self, order) -> None:
        for pokemon in order:
            trainer = self.trainer_of_active_pokemon(pokemon)
            pokemon_pos = trainer.active_pokemon.index(pokemon)
            if pokemon.secondary_status['Ingrained']:
                heal_ratio = pokemon.stats['hp'] // 16

                heal_amnt = (heal_ratio if heal_ratio > 1 else 1) \
                    if (pokemon.stats['hp'] - pokemon.current_hp) < heal_ratio \
                    else (pokemon.stats['hp'] - pokemon.current_hp)

                pokemon.current_hp += heal_amnt
                print(
                    f"{trainer.trainer_name}'s {pokemon.species_name} absorbed nutrients with its roots!")

            if trainer.field['Wish'][pokemon_pos] > 1:
                trainer.field['Wish'][pokemon_pos] -= 1
            elif trainer.field['Wish'][pokemon_pos] == 1:
                heal_ratio = pokemon.stats['hp'] // 2

                heal_amnt = (heal_ratio if heal_ratio > 1 else 1) \
                    if (pokemon.stats['hp']-pokemon.current_hp) < heal_ratio \
                    else (pokemon.stats['hp']-pokemon.current_hp)

                pokemon.current_hp += heal_amnt
                trainer.field['Wish'][pokemon_pos] -= 1

            fut_sight_turns = trainer.field['Future Sight'][pokemon_pos]['turns']
            if fut_sight_turns > 1:
                fut_sight_turns -= 1
            elif fut_sight_turns == 1:
                dmg_deal_pokemon = trainer.field['Future Sight'][pokemon_pos]['attacker']
                damage = self.dmg_calc(
                    pokemon, dmg_deal_pokemon, future_sight())
                chance_of_hit = future_sight().accuracy / 100 *
                is_hitting = random.random(0, 1)
                if future_sight().accuracy / 100
                pokemon.current_hp -= damage

                # -----------
            elif trainer.field['Future Sight'][self.trainer_of_active_pokemon(pokemon).active_pokemon.index(pokemon)][0] == 1:
                pokemon.current_hp -= (self.dmg_calc(pokemon, self.trainer_of_active_pokemon(pokemon).field['Future Sight'][self.trainer_of_active_pokemon(pokemon).active_pokemon.index(pokemon)][1], Move('Future Sight', 80, 15, 'Psychic', 90, 'Special', False, {'atk': 0, 'def': 0, 'spatk': 0, 'spdef': 0, 'spd': 0}, {'atk': 0, 'def': 0, 'spatk': 0, 'spdef': 0, 'spd': 0}))) if (
                    self.dmg_calc(pokemon, self.trainer_of_active_pokemon(pokemon).field['Future Sight'][self.trainer_of_active_pokemon(pokemon).active_pokemon.index(pokemon)][1], Move('Future Sight', 80, 15, 'Steel', 90, 'Special', False, {'atk': 0, 'def': 0, 'spatk': 0, 'spdef': 0, 'spd': 0}, {'atk': 0, 'def': 0, 'spatk': 0, 'spdef': 0, 'spd': 0})) < pokemon.current_hp) else pokemon.current_hp
                self.trainer_of_active_pokemon(pokemon).field['Future Sight'][self.trainer_of_active_pokemon(
                    pokemon).active_pokemon.index(pokemon)][0] -= 1
            if self.trainer_of_active_pokemon(pokemon).field['Doom Desire'][self.trainer_of_active_pokemon(pokemon).active_pokemon.index(pokemon)][0] > 1:
                self.trainer_of_active_pokemon(pokemon).field['Doom Desire'][self.trainer_of_active_pokemon(
                    pokemon).active_pokemon.index(pokemon)][0] -= 1
            elif self.trainer_of_active_pokemon(pokemon).field['Doom Desire'][self.trainer_of_active_pokemon(pokemon).active_pokemon.index(pokemon)][0] == 1:
                pokemon.current_hp -= (self.dmg_calc(pokemon, self.trainer_of_active_pokemon(pokemon).field['Doom Desire'][self.trainer_of_active_pokemon(pokemon).active_pokemon.index(pokemon)][1], Move('Doom Desire', 80, 15, 'Steel', 90, 'Special', False, {'atk': 0, 'def': 0, 'spatk': 0, 'spdef': 0, 'spd': 0}, {'atk': 0, 'def': 0, 'spatk': 0, 'spdef': 0, 'spd': 0}))) if (self.dmg_calc(
                    pokemon, self.trainer_of_active_pokemon(pokemon).field['Doom Desire'][self.trainer_of_active_pokemon(pokemon).active_pokemon.index(pokemon)][1], Move('Doom Desire', 80, 15, 'Steel', 90, 'Special', False, {'atk': 0, 'def': 0, 'spatk': 0, 'spdef': 0, 'spd': 0}, {'atk': 0, 'def': 0, 'spatk': 0, 'spdef': 0, 'spd': 0})) < pokemon.current_hp) else pokemon.current_hp
                self.trainer_of_active_pokemon(pokemon).field['Doom Desire'][self.trainer_of_active_pokemon(
                    pokemon).active_pokemon.index(pokemon)][0] -= 1

    def turn_effects(self) -> None:
        order = self.turn_order()
        self.weather_turn_effects(order)
        self.status_turn_effects(order)
        self.secondary_status_turn_effects(order)
        self.tertiary_status_turn_effects(order)

    def safe_switch(self, fainted_pokemon: Pokemon, switch_pokemon: Pokemon) -> None:
        fainted_pokemon.active = False
        switch_pokemon.active = True
        trainer = self.trainer_of_active_pokemon(fainted_pokemon)
        position = trainer.active_pokemon.index(fainted_pokemon)
        trainer.active_pokemon[position] = switch_pokemon

    def battle(self) -> None:
        print(
            f'{self.trainers[0].trainer_name} vs {self.trainers[1].trainer_name} begins...')

        for trainer in self.trainers:
            trainer.active_pokemon[0] = trainer.pokemon_list[0]
            trainer.active_pokemon[0].active = True

            if self.battle_mode == 2:
                trainer.active_pokemon[1] = trainer.pokemon_list[1]
                trainer.active_pokemon[1].active = True
                print(
                    f'{trainer.trainer_name} sents out {trainer.active_pokemon[0]} and {trainer.active_pokemon[1]}!')
            else:
                print(
                    f'{trainer.trainer_name} sents out {trainer.active_pokemon[0]}!')

        while not self.trainers[0].is_defeated or not self.trainers[1].is_defeated:
            self.turn_effects()
            self.battle_turn += 1
            print('Battle Turn: ', self.battle_turn)
            order = self.turn_order()
            for pokemon in order:
                moves = pokemon.move_list
                switch = None
                items = None
                for trainer in self.trainers:
                    if pokemon in trainer.active_pokemon:
                        switch = trainer.pokemon_list.copy().remove(pokemon)
                        if self.battle_mode == 2:
                            switch = switch.remove(
                                trainer.active_pokemon.copy().remove(pokemon)[0])
                        items = trainer.usable_items
                print(f'Choose the move(m1-m4):')
                for move in moves:
                    print(f'{move.move_name}', end='\t')
                print(f'Switch Pokemon(p1-p6):')
                for pokemon_switchable in switch:
                    print(
                        f'{pokemon_switchable.species_name}(lv:{pokemon_switchable.level})', end='   ')
                print(f'Items')
