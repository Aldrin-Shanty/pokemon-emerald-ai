def tri_status(name: str) -> float:
    tri_status = ["Tri Attack"]

    if name in tri_status:
        return 0.2
    else:
        return 0.0


def prlz_move(name: str) -> float:
    paralysis_moves = {
        "Body Slam": 0.3,
        "Bounce": 0.3,
        "Dragon Breath": 0.3,
        "Glare": 1.0,
        "Lick": 0.3,
        "Spark": 0.3,
        "Stun Spore": 1.0,
        "Thunder": 0.3,
        "Thunderbolt": 0.1,
        "Thunder Punch": 0.1,
        "Thunder Shock": 0.1,
        "Thunder Wave": 1.0,
        "Zap Cannon": 0.1
    }

    if name in paralysis_moves:
        return paralysis_moves[name]
    else:
        return 0


def hit_flyer(name: str) -> int:
    hit_flyers = {
        "Gust": 2,
        "Sky Uppercut": 1,
        "Thunder": 1,
        "Twister": 2,
    }

    if name in hit_flyers:
        return hit_flyers[name]
    else:
        return 0


def recoil(name: str) -> float:
    recoil = {
        "Volt Tackle": 0.3,
        "Take Down": 0.25,
        "Submission": 0.25,
        "Struggle": 0.25,
        "Double-Edge": 0.3,
    }

    if name in recoil:
        return recoil[name]
    else:
        return 0


def move_lock(name: str) -> list[int, int]:
    move_lock = {
        "Ice Ball": [5, 5],
        "Outrage": [2, 3],
        "Petal Dance": [2, 3],
        "Rollot": [5, 5],
        "Thrash": [2, 3],
        "Uproar": [2, 5]
    }

    if name in move_lock:
        return move_lock[name]
    else:
        return [1, 1]


def dmg_increase(name: str) -> bool:
    dmg_increase = [
        "Ice Ball",
        "Rollout"
    ]

    if name in dmg_increase:
        return True
    else:
        return False


def counter_attack(name: str) -> str:
    counter_attack = {
        "Bide": "Both",
        "Counter": "Physical",
        "Mirror Coat": "Special"
    }

    if name in counter_attack:
        return counter_attack[name]
    else:
        return None


def hazard(name: str) -> bool:
    hazard = ["Spikes"]

    if name in hazard:
        return True
    else:
        return False


def hazard_rem(name: str) -> bool:
    hazard_rem = ["Radpid Spin"]

    if name in hazard_rem:
        return True
    else:
        return False


def friendship(name: str) -> bool:
    friendship = ["Return", "Frustration"]

    if name in friendship:
        return True
    else:
        return False


def weather_change(name: str) -> str:
    weather_change = {
        "Hail": "Hail",
        "Rain Dance": "Rainy",
        "Sunny Day": "Sunny",
        "Sandstorm": "Sandstorm"
    }

    if name in weather_change:
        return weather_change[name]
    else:
        return None


def perma_trap(name: str) -> bool:
    perma_trap = {
        "Ingrain": "Self",
        "Block": "Enemy",
        "Mean Look": "Enemy",
    }

    if name in perma_trap:
        return perma_trap[name]
    else:
        return None


def crit_raise(name: str) -> bool:
    crit_raise = ["Focus Energy"]

    if name in crit_raise:
        return True
    else:
        return False


def inf_accuracy(name: str) -> bool:
    inf_acc = [
        'Aerial Ace',
        'Bide',
        'Block',
        'Conversion 2',
        'Feint Attack',
        'Foresight',
        'Lock-On',
        'Magical Leaf',
        'Mean Look',
        'Memento',
        'Mimic',
        'Mind Reader',
        'Miracle Eye',
        'Nightmare',
        'Odor Sleuth',
        'Pain Split',
        'Psych Up',
        'Roar',
        'Role Play',
        'Shadow Punch',
        'Shock Wave',
        'Sketch',
        'Skill Swap',
        'Swift',
        'Telekinesis',
        'Transform',
        'Whirlwind',
        'Yawn'
    ]

    if name in inf_acc:
        return True
    else:
        return False


def weather_inf_acc(name: str) -> str:
    weather_inf_acc = {
        "Thunder": "Rainy",
        "Blizzard": "Hail",
    }

    if name in weather_inf_acc:
        return weather_inf_acc[name]
    else:
        return None


def minimize_inf_acc(name: str) -> bool:
    minimize_inf_acc = ["Body Slam", "Stomp"]

    if name in minimize_inf_acc:
        return True
    else:
        return False


def psntype_inf_acc(name: str) -> bool:
    psntype_inf_acc = ['Toxic']
    if name in psntype_inf_acc:
        return True
    else:
        return False


def faint_user(name: str) -> bool:
    faint_user = ['Memento', 'Explosion', 'Self-Destruct']

    if name in faint_user:
        return True
    else:
        return False


def hp_cost(name: str) -> float:
    hp_cost = {
        "Belly Drum": 0.5,
        "Substitute": 0.25
    }

    if name in hp_cost:
        return hp_cost[name]
    else:
        return 0


def direct_dmg(name: str) -> int:
    direct_dmg = {
        "Dragon Rage": 40,
        "Sonic Boom": 20,
    }

    if name in direct_dmg:
        return direct_dmg[name]
    else:
        return 0


def level_direct_dmg(name: str) -> int:
    level_direct_dmg = ['Seismic Toss', 'NightShade', 'Psywave']

    if name in level_direct_dmg:
        return True
    else:
        return False


def percent_health_direct_dmg(name: str) -> float:
    percent_health_direct_dmg = {"Super Fang": 0.5}

    if name in percent_health_direct_dmg:
        return percent_health_direct_dmg(name)
    else:
        return 0.0


def user_health_direct_dmg(name: str) -> bool:
    user_health_direct_dmg = ["Endeavor"]

    if name in user_health_direct_dmg:
        return True
    else:
        return False
