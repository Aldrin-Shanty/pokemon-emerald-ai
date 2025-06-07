class Move:

    def __init__(self,move_name,base_power,power_points,type_of_move,accuracy_of_move,category_of_move,
                 has_contact=False,user_stat_change=None,enemy_stat_change=None,no_of_targets=1,
                 recoil=0,priority = 0,no_of_hits=1,crit_chance=0.0625):

        self.move_name=move_name
        self.base_power=base_power
        self.max_power_points=power_points
        self.power_points=power_points
        self.type=type_of_move
        self.no_of_hits=no_of_hits #1-5
        self.crit_chance=crit_chance
        self.accuracy=accuracy_of_move
        self.category=category_of_move # 'Special' 'Physical' 'Status'
        self.has_contact=has_contact
        self.priority=priority
        self.recoil = recoil # recoil percent of health

        self.user_stat_change=user_stat_change \
            if user_stat_change \
            else {'atk':0,'def':0,'spatk':0,'spdef':0,'spd':0,'evs':0,'acc':0}

        self.enemy_stat_change=enemy_stat_change \
            if enemy_stat_change \
            else {'atk':0,'def':0,'spatk':0,'spdef':0,'spd':0,'evs':0,'acc':0}

        self.no_of_targets=no_of_targets