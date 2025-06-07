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
        self.field={'spikes':0,'reflect':0,'lightscreen':0,'Wish':[0,0],'Future Sight':[[0,None],[0,None]],'Doom Desire':[[0,None],[0,None]]} #[no of turns for pos 1, no of turns for pos 2]
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
        self.active_pokemon[user_pos-1].selected_move=move_used
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