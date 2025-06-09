def hits(name: str) -> list[int, int]:
    hit_2_5 = [
        "Arm Thrust",
        "Barrage",
        "Bone Rush",
        "Bullet Seed",
        "Comet Punch",
        "Double Slap",
        "Fury Attack",
        "Fury Swipes",
        "Icicle Spear",
        "Pin Missile",
        "Rock Blast",
        "Spike Cannon"
    ]
    hit_2 = [
        "Double Kick",
        "Bonemerang",
        "Twineedle"
    ]
    hit_3 = [
        "Triple Kick"
    ]
    if name in hit_2_5:
        return [2, 5]
    elif name in hit_2:
        return [2, 2]
    elif name in hit_3:
        return [3, 3]
    else:
        return [1, 1]


def crit_chance(name: str) -> float:
    crit_chance = 0.0625

    high_crit = [
        "Aeroblast",
        "Air Cutter",
        "Blaze Kick",
        "Crabhammer",
        "Cross Chop",
        "Karate Chop",
        "Leaf Blade",
        "Poison Tail",
        "Razor Leaf",
        "Razor Wind",
        "Sky Attack",
        "Slash"
    ]

    if name in high_crit:
        return crit_chance*2
    else:
        return crit_chance


def contact(name: str) -> bool:
    is_contact = [
        "Aerial Ace", "Arm Thrust", "Astonish", "Bide", "Bind", "Bite", "Blaze Kick", "Body Slam",
        "Bounce", "Brick Break", "Clamp", "Comet Punch", "Constrict", "Counter", "Covet", "Crabhammer",
        "Cross Chop", "Crunch", "Crush Claw", "Cut", "Dig", "Dive", "Dizzy Punch", "Double-Edge",
        "Double Kick", "Double Slap", "Dragon Claw", "Drill Peck", "Dynamic Punch", "Endeavor",
        "Extreme Speed", "Facade", "Fake Out", "False Swipe", "Feint Attack", "Fire Punch", "Flail",
        "Flame Wheel", "Fly", "Focus Punch", "Frustration", "Fury Attack", "Fury Cutter", "Fury Swipes",
        "Guillotine", "Headbutt", "High Jump Kick", "Horn Attack", "Horn Drill", "Hyper Fang",
        "Ice Ball", "Ice Punch", "Iron Tail", "Jump Kick", "Karate Chop", "Knock Off", "Leaf Blade",
        "Leech Life", "Lick", "Low Kick", "Mach Punch", "Megahorn", "Mega Kick", "Mega Punch",
        "Metal Claw", "Meteor Mash", "Needle Arm", "Outrage", "Peck", "Petal Dance", "Poison Fang",
        "Poison Tail", "Pound", "Pursuit", "Quick Attack", "Rage", "Rapid Spin", "Return", "Revenge",
        "Reversal", "Rock Smash", "Rolling Kick", "Rollout", "Scratch", "Seismic Toss", "Shadow Punch",
        "Skull Bash", "Sky Uppercut", "Slam", "Slash", "Smelling Salts", "Spark", "Steel Wing",
        "Stomp", "Strength", "Struggle", "Submission", "Super Fang", "Superpower", "Tackle", "Take Down",
        "Thief", "Thrash", "Thunder Punch", "Triple Kick", "Vice Grip", "Vine Whip", "Vital Throw",
        "Volt Tackle", "Waterfall", "Wing Attack", "Wrap"
    ]
    if name in is_contact:
        return True
    else:
        return False


def charge_turn(name: str) -> list[int, bool]:
    # [no of turns to charge,is invulnerable]
    charge_turn = {
        'Bounce': [1, True],
        'Dig': [1, True],
        'Dive': [1, True],
        'Fly': [1, True],
        'Razor Wind': [1, False],
        'Skull Bash': [1, False],
        'Sky Attack': [1, False],
        'Solar Beam': [1, False],
        "Bide": [2, False]
    }

    if name in charge_turn:
        return charge_turn[name]
    else:
        return [0, False]


def recharge(name: str) -> bool:
    recharge = ['Blast Burn', 'Frenzy Plant', 'Hydro Cannon', 'Hyper Beam']

    if name in recharge:
        return True
    else:
        return False


def ign_protect(name: str) -> bool:
    ign_protect = [
        "Acid Armor", "Agility", "Amnesia", "Aromatherapy", "Assist", "Barrier", "Baton Pass",
        "Belly Drum", "Block", "Bulk Up", "Calm Mind", "Camouflage", "Charge", "Conversion",
        "Conversion 2", "Cosmic Power", "Curse", "Defense Curl", "Destiny Bond", "Detect",
        "Doom Desire", "Double Team", "Dragon Dance", "Endure", "Focus Energy", "Follow Me",
        "Future Sight", "Growth", "Grudge", "Hail", "Harden", "Haze", "Heal Bell", "Helping Hand",
        "Howl", "Imprison", "Ingrain", "Iron Defense", "Light Screen", "Magic Coat", "Mean Look",
        "Meditate", "Metronome", "Milk Drink", "Minimize", "Mirror Move", "Mist", "Moonlight",
        "Morning Sun", "Mud Sport", "Nature Power", "Perish Song", "Protect", "Psych Up",
        "Rain Dance", "Recover", "Recycle", "Reflect", "Refresh", "Rest", "Roar", "Role Play",
        "Safeguard", "Sandstorm", "Sharpen", "Sketch", "Slack Off", "Sleep Talk", "Snatch",
        "Soft-Boiled", "Spikes", "Splash", "Stockpile", "Substitute", "Sunny Day", "Swallow",
        "Swords Dance", "Synthesis", "Tail Glow", "Teleport", "Transform", "Water Sport",
        "Whirlwind", "Wish", "Withdraw"
    ]

    if name in ign_protect:
        return True
    else:
        return False


def snatchable(name: str) -> bool:
    snatchable = [
        "Acid Armor", "Agility", "Amnesia", "Aromatherapy", "Barrier", "Belly Drum",
        "Bulk Up", "Calm Mind", "Camouflage", "Charge", "Conversion", "Cosmic Power",
        "Defense Curl", "Double Team", "Dragon Dance", "Focus Energy", "Growth", "Harden",
        "Heal Bell", "Howl", "Imprison", "Ingrain", "Iron Defense", "Light Screen",
        "Meditate", "Milk Drink", "Minimize", "Mist", "Moonlight", "Morning Sun", "Recover",
        "Recycle", "Reflect", "Refresh", "Rest", "Safeguard", "Sharpen", "Slack Off",
        "Soft-Boiled", "Stockpile", "Substitute", "Swallow", "Swords Dance", "Synthesis",
        "Tail Glow", "Wish", "Withdraw"
    ]

    if name in snatchable:
        return True
    else:
        return False


def copy_mirror(name: str) -> bool:
    copy_mirror = [
        "Absorb", "Acid", "Aerial Ace", "Aeroblast", "Air Cutter", "Ancient Power", "Arm Thrust",
        "Astonish", "Attract", "Aurora Beam", "Barrage", "Beat Up", "Bind", "Bite", "Blast Burn",
        "Blaze Kick", "Blizzard", "Block", "Body Slam", "Bone Club", "Bonemerang", "Bone Rush",
        "Bounce", "Brick Break", "Bubble", "Bubble Beam", "Bullet Seed", "Charm", "Clamp",
        "Comet Punch", "Confuse Ray", "Confusion", "Constrict", "Cotton Spore", "Covet",
        "Crabhammer", "Cross Chop", "Crunch", "Crush Claw", "Cut", "Dig", "Disable", "Dive",
        "Dizzy Punch", "Double-Edge", "Double Kick", "Double Slap", "Dragon Breath", "Dragon Claw",
        "Dragon Rage", "Dream Eater", "Drill Peck", "Dynamic Punch", "Earthquake", "Egg Bomb",
        "Ember", "Encore", "Endeavor", "Eruption", "Explosion", "Extrasensory", "Extreme Speed",
        "Facade", "Fake Out", "Fake Tears", "False Swipe", "Feather Dance", "Feint Attack",
        "Fire Blast", "Fire Punch", "Fire Spin", "Fissure", "Flail", "Flamethrower", "Flame Wheel",
        "Flash", "Flatter", "Fly", "Foresight", "Frenzy Plant", "Frustration", "Fury Attack",
        "Fury Cutter", "Fury Swipes", "Giga Drain", "Glare", "Grass Whistle", "Growl", "Guillotine",
        "Gust", "Headbutt", "Heat Wave", "Hidden Power", "High Jump Kick", "Horn Attack",
                "Horn Drill", "Hydro Cannon", "Hydro Pump", "Hyper Beam", "Hyper Fang", "Hyper Voice",
                "Hypnosis", "Ice Ball", "Ice Beam", "Ice Punch", "Icicle Spear", "Icy Wind", "Iron Tail",
                "Jump Kick", "Karate Chop", "Kinesis", "Knock Off", "Leaf Blade", "Leech Life",
                "Leech Seed", "Leer", "Lick", "Lock-On", "Lovely Kiss", "Low Kick", "Luster Purge",
                "Mach Punch", "Magical Leaf", "Magnitude", "Mean Look", "Mega Drain", "Megahorn",
                "Mega Kick", "Mega Punch", "Memento", "Metal Claw", "Metal Sound", "Meteor Mash",
                "Mind Reader", "Mist Ball", "Muddy Water", "Mud Shot", "Mud-Slap", "Needle Arm",
                "Nightmare", "Night Shade", "Octazooka", "Odor Sleuth", "Outrage", "Overheat",
                "Pain Split", "Pay Day", "Peck", "Petal Dance", "Pin Missile", "Poison Fang", "Poison Gas",
                "Poison Powder", "Poison Sting", "Poison Tail", "Pound", "Powder Snow", "Present",
                "Psybeam", "Psychic", "Psycho Boost", "Psywave", "Pursuit", "Quick Attack", "Rage",
                "Rapid Spin", "Razor Leaf", "Razor Wind", "Return", "Revenge", "Reversal", "Roar",
                "Rock Blast", "Rock Slide", "Rock Smash", "Rock Throw", "Rock Tomb", "Rolling Kick",
                "Rollout", "Sacred Fire", "Sand Attack", "Sand Tomb", "Scary Face", "Scratch", "Screech",
                "Secret Power", "Seismic Toss", "Self-Destruct", "Shadow Ball", "Shadow Punch",
                "Sheer Cold", "Shock Wave", "Signal Beam", "Silver Wind", "Sing", "Skill Swap",
                "Skull Bash", "Sky Attack", "Sky Uppercut", "Slam", "Slash", "Sleep Powder", "Sludge",
                "Sludge Bomb", "Smelling Salts", "Smog", "Smokescreen", "Snore", "Solar Beam",
                "Sonic Boom", "Spark", "Spider Web", "Spike Cannon", "Spite", "Spore", "Steel Wing",
                "Stomp", "Strength", "String Shot", "Stun Spore", "Submission", "Super Fang",
                "Superpower", "Supersonic", "Surf", "Swagger", "Sweet Kiss", "Sweet Scent", "Swift",
                "Tackle", "Tail Whip", "Take Down", "Taunt", "Teeter Dance", "Thief", "Thrash",
                "Thunder", "Thunderbolt", "Thunder Punch", "Thunder Shock", "Thunder Wave", "Tickle",
                "Torment", "Toxic", "Tri Attack", "Trick", "Triple Kick", "Twineedle", "Twister",
                "Uproar", "Vice Grip", "Vine Whip", "Vital Throw", "Volt Tackle", "Waterfall",
                "Water Gun", "Water Pulse", "Water Spout", "Weather Ball", "Whirlpool", "Whirlwind",
                "Will-O-Wisp", "Wing Attack", "Wrap", "Yawn", "Zap Cannon"
    ]

    if name in copy_mirror:
        return True
    else:
        return False


def sound_based(name: str) -> bool:
    sound_based = [
        "Grass Whistle",
        "Growl",
        "Heal Bell",
        "Hyper Voice",
        "Metal Sound",
        "Perish Song",
        "Roar",
        "Screech",
        "Sing",
        "Snore",
        "Supersonic",
        "Uproar"
    ]

    if name in sound_based:
        return True
    else:
        return False


def defrost(name: str) -> bool:
    defrost = ['Flame Wheel', 'Sacred Fire']

    if name in defrost:
        return True
    else:
        return False


def drain_moves(name: str) -> float:
    drain_moves = [
        "Absorb",
        "Dream Eater",
        "Giga Drain",
        "Leech Life",
        "Mega Drain",
    ]

    if name in drain_moves:
        return 0.5
    else:
        return 0.0


def healing_moves(name: str) -> float:
    healing_moves = {
        "Milk Drink": 0.5,
        "Moonlight": 0.5,
        "Morning Sun": 0.5,
        "Recover": 0.5,
        "Rest": 1,
        "Slack Off": 0.5,
        "Soft-Boiled": 0.5,
        "Swallow": 0.25,
        "Synthesis": 0.5,
        "Wish": 0.5,
    }

    if name in healing_moves:
        return healing_moves[name]
    else:
        return 0.0


def ign_sub(name: str) -> bool:
    ign_sub = [
        "Attract",
        "Conversion 2",
        "Curse",
        "Destiny Bond",
        "Disable",
        "Encore",
        "Foresight",
        "Grass Whistle",
        "Growl",
        "Grudge",
        "Haze",
        "Heal Bell",
        "Helping Hand",
        "Hyper Voice",
        "Imprison",
        "Metal Sound",
        "Mimic",
        "Odor Sleuth",
        "Perish Song",
        "Psych Up",
        "Roar",
        "Role Play",
        "Screech",
        "Sing",
        "Sketch",
        "Skill Swap",
        "Snatch",
        "Snore",
        "Spite",
        "Supersonic",
        "Taunt",
        "Torment",
        "Uproar",
        "Whirlwind"
    ]

    if name in ign_sub:
        return True
    else:
        return False


def trap_move(name: str) -> bool:
    trap_move = [
        "Bind",
        "Clamp",
        "Fire Spin",
        "Sand Tomb",
        "Whirlpool",
        "Wrap"
    ]

    if name in trap_move:
        return True
    else:
        return False


def force_switch(name: str) -> bool:
    force_switch = [
        "Roar",
        "Whirlwind"
    ]

    if name in force_switch:
        return True
    else:
        return False
