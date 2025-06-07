class Move:

    def __init__(self,move_name : str,base_power : int,power_points : int,type_of_move : str,accuracy_of_move : int,
                 category_of_move : str,has_contact : bool = False,user_stat_change : dict[str,int] = None,
                 enemy_stat_change : dict = None,no_of_targets : int = 1,recoil : int = 0,priority : float = 0.0,
                 no_of_hits : int = 1,crit_chance : int = 0.0625) -> None:

        self.move_name = move_name
        self.base_power = base_power
        self.max_power_points = power_points
        self.power_points = power_points
        self.type = type_of_move
        self.no_of_hits = no_of_hits #1-5
        self.crit_chance = crit_chance
        self.accuracy = accuracy_of_move
        self.category = category_of_move # 'Special' 'Physical' 'Status'
        self.has_contact = has_contact
        self.priority = priority
        self.recoil = recoil # recoil percent of health

        self.user_stat_change = user_stat_change \
            if user_stat_change \
            else {'atk':0,'def':0,'spatk':0,'spdef':0,'spd':0,'evs':0,'acc':0}

        self.enemy_stat_change = enemy_stat_change \
            if enemy_stat_change \
            else {'atk':0,'def':0,'spatk':0,'spdef':0,'spd':0,'evs':0,'acc':0}

        self.no_of_targets = no_of_targets