from battle_simulation.Functions.move_functions.move_attribute_1 import *
from battle_simulation.Functions.move_functions.move_attribute_2 import *


class Move:
    def __init__(self, move_name: str, base_power: int, power_points: int, type_of_move: str, accuracy_of_move: int, category: str, priority: float, targets: int) -> None:
        self.name = move_name
        self.base_power = base_power
        self.max_power_points = power_points
        self.power_points = power_points
        self.type = type_of_move
        self.accuracy = accuracy_of_move
        self.category = category
        self.priority = priority
        self.targets = targets

        self.hits = hits(self.name)
        self.crit_chance = crit_chance(self.name)
        self.contact = contact(self.name)
        self.charge_turn = charge_turn(self.name)
        self.recharge = recharge(self.name)
        self.ign_protect = ign_protect(self.name)
        self.snatchable = snatchable(self.name)
        self.copy_mirror = copy_mirror(self.name)
        self.sound_based = sound_based(self.name)
        self.defrost = defrost(self.name)
        self.drain_moves = drain_moves(self.name)
        self.healing_moves = healing_moves(self.name)
        self.ign_sub = ign_sub(self.name)
        self.trap_moves = trap_move(self.name)
        self.force_switch = force_switch(self.name)
        self.tri_status = tri_status(self.name)
        self.prlz_move = prlz_move(self.name)
        self.hit_flyer = hit_flyer(self.name)
        self.recoil = recoil(self.name)
        self.move_lock = move_lock(self.name)
        self.dmg_increase = dmg_increase(self.name)
        self.counter_attack = counter_attack(self.name)
        self.hazard = hazard(self.name)
        self.hazard_rem = hazard_rem(self.name)
        self.friendship = friendship(self.name)
        self.weather_change = weather_change(self.name)
        self.perma_trap = perma_trap(self.name)
        self.crit_raise = crit_raise(self.name)
        self.inf_acc = inf_accuracy(self.name)
        self.weather_inf_acc = weather_inf_acc(self.name)
        self.minimize_inf_acc = minimize_inf_acc(self.name)
        self.psntype_inf_acc = psntype_inf_acc(self.name)
