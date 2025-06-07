import random
from Move import Move
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
                    priority[i][j] += self.trainer_of_pokemon(pokemon).attacking[self.trainer_of_pokemon(pokemon).active_pokemon.index(pokemon)].priority
                priority[i][j]+= pokemons_temp.index(pokemon)/(len(pokemons_temp)-1)
        order=dict(zip([pokemon for trainer in pokemons for pokemon in trainer], [active_prio for trainer in priority for active_prio in trainer ]))
        order = sorted(order, key=order.get, reverse=True)
        return order

    def dmg_calc(self,dmg_taken_pokemon,dmg_deal_pokemon,move):
        """Calculate damage for moves used in the battle.

        Note:
            This method is currently a placeholder and needs implementation.
        """
        return 1

    def trainer_of_pokemon(self,pokemon):
        owner=None
        for trainer in self.trainers:
            if pokemon in trainer.active_pokemon:
                owner=trainer
        return owner

    def turn_effects(self):
        """Apply turn-based effects such as weather, status conditions, and field effects.

        Updates the state of weather, trainer fields, and Pokémon statuses.
        """
        order = self.turn_order
        for weather,turns in self.weather:
            if turns>1:
                if weather=='sunny':
                    print('The sunlight is strong')
                elif weather=='rainy':
                    print('It is raining')
                elif weather=='hail':
                    print('Hail continues to fall')
                    for pokemon in order:
                        if pokemon.type[0] in ['Ice'] or pokemon.type[1] in ['Ice']:
                            pokemon.current_hp-=(pokemon.stats['hp']//16 if pokemon.stats['hp']//16 >1 else 1) if pokemon.current_hp < pokemon.stats['hp']//16 else pokemon.current_hp
                            print(f"{self.trainer_of_pokemon(pokemon).trainer_name}'s {pokemon.species_name} was buffeted by hail")
                elif weather=='sandstorm':
                    print('The sandstorm is raging')
                    for pokemon in order:
                        if pokemon.type[0] in ['Rock','Ground','Steel'] or pokemon.type[1] in ['Rock','Ground','Steel']:
                            pokemon.current_hp-=(pokemon.stats['hp']//16 if pokemon.stats['hp']//16 >1 else 1) if pokemon.current_hp < pokemon.stats['hp']//16 else pokemon.current_hp
                            print(f"{self.trainer_of_pokemon(pokemon).trainer_name}'s {pokemon.species_name} was buffeted by sandstorm")
                turns -= 1
            elif turns==1:
                if weather=='sunny':
                    print('The sunlight faded')
                elif weather=='rainy':
                    print('The rain stopped')
                elif weather=='hail':
                    print('The hail subsided')
                elif weather=='sandstorm':
                    print('The sandstorm subsided')
                turns -= 1
        for pokemon in order:
            pokemon.current_hp-=((pokemon.stats['hp']//16 if pokemon.stats['hp']//16 >1 else 1) if pokemon.current_hp < pokemon.stats['hp']//16 else pokemon.current_hp) if (pokemon.status['psn'] or pokemon.status['brn']) else pokemon.current_hp
            pokemon.current_hp-=((pokemon.stats['hp']*(pokemon.status['bdpsn']+1)//16 if pokemon.stats['hp']*(pokemon.status['bdpsn']+1)//16>1 else 1) if pokemon.current_hp < pokemon.stats['hp']*(pokemon.status['bdpsn']+1)//16 else pokemon.current_hp) if (pokemon.status['bdpsn']) else pokemon.current_hp
            pokemon.status['bdpsn']+=1
            if pokemon.status['brn']:
                print(f"{self.trainer_of_pokemon(pokemon).trainer_name}'s {pokemon.species_name} was hurt by burn")
            if pokemon.status['psn'] or pokemon.status['bdpsn']:
                print(f"{self.trainer_of_pokemon(pokemon).trainer_name}'s {pokemon.species_name} was hurt by poison")
            pokemon.status['slp']-=1 if pokemon.status['slp'] else 0
            pokemon.status['frz'] -= 1 if pokemon.status['frz'] else 0
        for pokemon in order:
            if pokemon.secondary_status['Leech Seeded'][0]:
                self.trainers[-(self.trainers.index(self.trainer_of_pokemon(pokemon))+1)].active_pokemon[pokemon.secondary_status['Leech Seeded'][1]].currenth_hp+= (pokemon.stats['hp']//8 if pokemon.stats['hp']//8 >1 else 1) if pokemon.current_hp < pokemon.stats['hp']//8 else pokemon.current_hp
                pokemon.current_hp-= (pokemon.stats['hp']//8 if pokemon.stats['hp']//8 >1 else 1) if pokemon.current_hp < pokemon.stats['hp']//8 else pokemon.current_hp
                print(f"{self.trainer_of_pokemon(pokemon).trainer_name}'s {pokemon.species_name} health is sapped by {self.trainers[-(self.trainers.index(self.trainer_of_pokemon(pokemon))+1)].trainer_name}'s {self.trainers[-(self.trainers.index(self.trainer_of_pokemon(pokemon))+1)].active_pokemon[pokemon.secondary_status['Leech Seeded'][1]].species_name}")
            if pokemon.secondary_status['Perish Song']>1:
                print(f"{self.trainer_of_pokemon(pokemon).trainer_name}'s {pokemon.species_name} perish count has fallen to {pokemon.secondary_status['Perish Song']-1}")
                pokemon.secondary_status['Perish Song']-=1
            elif pokemon.secondary_status['Perish Song']==1:
                pokemon.current_hp=0
                pokemon.secondary_status['Perish Song']-=1
            if pokemon.secondary_status['Yawn'] >1:
                pokemon.secondary_status['Yawn']-=1
            elif pokemon.secondary_status['Yawn']==1:
                pokemon.status['slp']= random.randint(1,4)
                pokemon.secondary_status['Yawn']-=1
            if pokemon.secondary_status['Partially Trapped']>1:
                pokemon.current_hp-=(pokemon.stats['hp']//16 if pokemon.stats['hp']//16 >1 else 1) if pokemon.current_hp < pokemon.stats['hp']//16 else pokemon.current_hp
                print(f"{self.trainer_of_pokemon(pokemon).trainer_name}'s {pokemon.species_name} is hurt by the traps")
                pokemon.secondary_status['Partially Trapped']-=1
            elif pokemon.secondary_status['Partially Trapped']==1:
                print(f"{self.trainer_of_pokemon(pokemon).trainer_name}'s {pokemon.species_name} was freed from the traps")
                pokemon.secondary_status['Partially Trapped']-=1
        for pokemon in order:
            if pokemon.secondary_status['Ingrained']:
                pokemon.current_hp += (pokemon.stats['hp'] // 16 if pokemon.stats['hp'] // 16 > 1 else 1) if (pokemon.stats['hp']-pokemon.current_hp) < (pokemon.stats['hp'] // 16) else (pokemon.stats['hp']-pokemon.current_hp)
                print(f"{self.trainer_of_pokemon(pokemon).trainer_name}'s {pokemon.species_name} absorbed nutrients with its roots!")
            if self.trainer_of_pokemon(pokemon).field['Wish'][self.trainer_of_pokemon(pokemon).active_pokemon.index(pokemon)]>1:
                self.trainer_of_pokemon(pokemon).field['Wish'][self.trainer_of_pokemon(pokemon).active_pokemon.index(pokemon)]-=1
            elif self.trainer_of_pokemon(pokemon).field['Wish'][self.trainer_of_pokemon(pokemon).active_pokemon.index(pokemon)]==1:
                pokemon.current_hp += (pokemon.stats['hp'] // 2 if pokemon.stats['hp'] // 2 > 1 else 1) if (pokemon.stats['hp']-pokemon.current_hp) < (pokemon.stats['hp'] // 2) else (pokemon.stats['hp']-pokemon.current_hp)
                self.trainer_of_pokemon(pokemon).field['Wish'][self.trainer_of_pokemon(pokemon).active_pokemon.index(pokemon)]-=1
            if self.trainer_of_pokemon(pokemon).field['Future Sight'][self.trainer_of_pokemon(pokemon).active_pokemon.index(pokemon)][0]>1:
                self.trainer_of_pokemon(pokemon).field['Future Sight'][self.trainer_of_pokemon(pokemon).active_pokemon.index(pokemon)][0]-=1
            elif self.trainer_of_pokemon(pokemon).field['Future Sight'][self.trainer_of_pokemon(pokemon).active_pokemon.index(pokemon)][0]==1:
                pokemon.current_hp -= (self.dmg_calc(pokemon,self.trainer_of_pokemon(pokemon).field['Future Sight'][self.trainer_of_pokemon(pokemon).active_pokemon.index(pokemon)][1],Move('Future Sight',80,15,'Psychic',90,'Special',False,{'atk':0,'def':0,'spatk':0,'spdef':0,'spd':0},{'atk':0,'def':0,'spatk':0,'spdef':0,'spd':0}))) if (self.dmg_calc(pokemon,self.trainer_of_pokemon(pokemon).field['Future Sight'][self.trainer_of_pokemon(pokemon).active_pokemon.index(pokemon)][1],Move('Future Sight',80,15,'Steel',90,'Special',False,{'atk':0,'def':0,'spatk':0,'spdef':0,'spd':0},{'atk':0,'def':0,'spatk':0,'spdef':0,'spd':0})) < pokemon.current_hp) else pokemon.current_hp
                self.trainer_of_pokemon(pokemon).field['Future Sight'][self.trainer_of_pokemon(pokemon).active_pokemon.index(pokemon)][0]-=1
            if self.trainer_of_pokemon(pokemon).field['Doom Desire'][self.trainer_of_pokemon(pokemon).active_pokemon.index(pokemon)][0]>1:
                self.trainer_of_pokemon(pokemon).field['Doom Desire'][self.trainer_of_pokemon(pokemon).active_pokemon.index(pokemon)][0]-=1
            elif self.trainer_of_pokemon(pokemon).field['Doom Desire'][self.trainer_of_pokemon(pokemon).active_pokemon.index(pokemon)][0]==1:
                pokemon.current_hp -= (self.dmg_calc(pokemon,self.trainer_of_pokemon(pokemon).field['Doom Desire'][self.trainer_of_pokemon(pokemon).active_pokemon.index(pokemon)][1],Move('Doom Desire',80,15,'Steel',90,'Special',False,{'atk':0,'def':0,'spatk':0,'spdef':0,'spd':0},{'atk':0,'def':0,'spatk':0,'spdef':0,'spd':0}))) if (self.dmg_calc(pokemon,self.trainer_of_pokemon(pokemon).field['Doom Desire'][self.trainer_of_pokemon(pokemon).active_pokemon.index(pokemon)][1],Move('Doom Desire',80,15,'Steel',90,'Special',False,{'atk':0,'def':0,'spatk':0,'spdef':0,'spd':0},{'atk':0,'def':0,'spatk':0,'spdef':0,'spd':0})) < pokemon.current_hp) else pokemon.current_hp
                self.trainer_of_pokemon(pokemon).field['Doom Desire'][self.trainer_of_pokemon(pokemon).active_pokemon.index(pokemon)][0]-=1
    def safe_switch(self,fainted_pokemon,switch_pokemon):
        self.trainer_of_pokemon(fainted_pokemon).active_pokemon[self.trainer_of_pokemon(fainted_pokemon).active_pokemon.index(fainted_pokemon)]=switch_pokemon

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
                print(f'Choose the move(m1-m4):')
                for move in moves:
                    print(f'{move.move_name}',end='\t')
                print(f'Switch Pokemon(p1-p6):')
                for pokemon_switchable in switch:
                    print(f'{pokemon_switchable.species_name}(lv:{pokemon_switchable.level})',end='   ')
                print(f'Items')