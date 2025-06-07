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