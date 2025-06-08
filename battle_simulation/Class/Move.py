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

        if self.name in hit_2_5:
            self.hits = [2, 5]
        elif self.name in hit_2:
            self.hits = [2, 2]
        elif self.name in hit_3:
            self.hits = [3, 3]
        else:
            self.hits = [1, 1]

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

        if self.name in high_crit:
            self.crit_chance = crit_chance*2
        else:
            self.crit_chance = crit_chance

        contact = [
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

        if self.name in contact:
            self.contact = True
        else:
            self.contact = False
        # [no of turns to charge,is invincible]
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

        if self.name in charge_turn:
            self.charge_turn = charge_turn[self.name]
        else:
            self.charge_turn = [0, False]

        recharge = ['Blast Burn', 'Frenzy Plant', 'Hydro Cannon', 'Hyper Beam']

        if self.name in recharge:
            self.recharge = True
        else:
            self.recharge = False

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

        if self.name in ign_protect:
            self.ign_protect = True
        else:
            self.ign_protect = False

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

        if self.name in snatchable:
            self.snatchable = True
        else:
            self.snatchable = False

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

        if self.name in copy_mirror:
            self.copy_mirror = True
        else:
            self.copy_mirror = False

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

        if self.name in sound_based:
            self.sound_based = True
        else:
            self.sound_based = False

        defrost = ['Flame Wheel', 'Sacred Fire']

        if self.name in defrost:
            self.defrost = True
        else:
            self.defrost = False

        drain_moves = [
            "Absorb",
            "Dream Eater",
            "Giga Drain",
            "Leech Life",
            "Mega Drain",
        ]

        if self.name in drain_moves:
            self.drain_moves = 0.5
        else:
            self.drain_moves = 0

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

        if self.name in healing_moves:
            self.healing_move = healing_moves[self.name]
        else:
            self.healing_move = 0

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

        if self.name in ign_sub:
            self.ign_sub = True
        else:
            self.ign_sub = False

        trap_move = [
            "Bind",
            "Clamp",
            "Fire Spin",
            "Sand Tomb",
            "Whirlpool",
            "Wrap"
        ]

        if self.name in trap_move:
            self.trap_move = True
        else:
            self.trap_move = False

        force_switch = [
            "Roar",
            "Whirlwind"
        ]

        if self.name in force_switch:
            self.force_switch = True
        else:
            self.force_switch = False

        tri_status = ["Tri Attack"]

        if self.name in tri_status:
            self.tri_status = 0.2
        else:
            self.tri_status = 0

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

        if self.name in paralysis_moves:
            self.prlz_move = paralysis_moves[self.name]
        else:
            self.prlz_move = 0

        hit_flyers = {
            "Gust": 2,
            "Sky Uppercut": 1,
            "Thunder": 1,
            "Twister": 2,
        }

        if self.name in hit_flyers:
            self.hit_flyer = hit_flyers[self.name]
        else:
            self.hit_flyer = 0

        recoil = {
            "Volt Tackle": 0.3,
            "Take Down": 0.25,
            "Submission": 0.25,
            "Struggle": 0.25,
            "Double-Edge": 0.3,
        }

        if self.name in recoil:
            self.recoil = recoil[self.name]
        else:
            self.recoil = 0

        move_lock = {
            "Ice Ball": [5, 5],
            "Outrage": [2, 3],
            "Petal Dance": [2, 3],
            "Rollot": [5, 5],
            "Thrash": [2, 3],
            "Uproar": [2, 5]
        }

        if self.name in move_lock:
            self.move_lock = move_lock[self.name]
        else:
            self.move_lock = [1, 1]

        dmg_increase = [
            "Ice Ball",
            "Rollout"
        ]

        if self.name in dmg_increase:
            self.dmg_increase = True
        else:
            self.dmg_increase = False

        counter_attack = {
            "Bide": "Both",
            "Counter": "Physical",
            "Mirror Coat": "Special"
        }

        if self.name in counter_attack:
            self.counter_attack = counter_attack[self.name]
        else:
            self.counter_attack = None

        hazard = ["Spikes"]

        if self.name in hazard:
            self.hazard = True
        else:
            self.hazard = False

        hazard_rem = ["Radpid Spin"]

        if self.name in hazard_rem:
            self.hazard_rem = True
        else:
            self.hazard_rem = False

        friendship = ["Return", "Frustration"]

        if self.name in friendship:
            self.friendship = True
        else:
            self.friendship = False

        weather_change = {
            "Hail": "Hail",
            "Rain Dance": "Rainy",
            "Sunny Day": "Sunny",
            "Sandstorm": "Sandstorm"
        }

        if self.name in weather_change:
            self.weather_change = weather_change[self.name]

        perma_trap = {
            "Ingrain": "Self",
            "Block": "Enemy",
            "Mean Look": "Enemy",
        }

        if self.name in perma_trap:
            self.perma_trap = perma_trap[self.name]
        else:
            self.perma_trap = None

        crit_raise = ["Focus Energy"]

        if self.name in crit_raise:
            self.crit_raise = True
        else:
            self.crit_raise = False

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

        if self.name in inf_acc:
            self.inf_acc = True
        else:
            self.inf_acc = False

        weather_inf_acc = {
            "Thunder": "Rainy",
            "Blizzard": "Hail",
        }

        if self.name in weather_inf_acc:
            self.weather_inf_acc = weather_inf_acc[self.name]
        else:
            self.weather_inf_acc = None

        minimize_inf_acc = ["Body Slam", "Stomp"]

        if self.name in minimize_inf_acc:
            self.minimize_inf_acc = True
        else:
            self.minimize_inf_acc = False

        psntype_inf_acc = ['Toxic']
        if self.name in psntype_inf_acc:
            self.psntype_inf_acc = True
        else:
            self.psntype_inf_acc = False

        faint_user = ['Memento', 'Explosion', 'Self-Destruct']

        if self.name in faint_user:
            self.faint_user = True
        else:
            self.faint_user = False

        hp_cost = {
            "Belly Drum": 0.5,
            "Substitute": 0.25
        }

        if self.name in hp_cost:
            self.hp_cost = hp_cost[self.name]
        else:
            self.hp_cost = 0

        direct_dmg = {
            "Dragon Rage": 40,
            "Sonic Boom": 20,
        }

        if self.name in direct_dmg:
            self.direct_dmg = direct_dmg[self.name]
        else:
            self.direct_dmg = 0

        level_direct_dmg = ['Seismic Toss', 'NightShade', 'Psywave']

        if self.name in level_direct_dmg:
            self.level_direct_dmg = True
        else:
            self.level_direct_dmg = False

        percent_health_direct_dmg = ["Super Fang"]

        if self.name in percent_health_direct_dmg:
            self.percent_health_direct_dmg = True
        else:
            self.percent_health_direct_dmg = False

        user_health_direct_dmg = ["Endeavor"]

        if self.name in user_health_direct_dmg:
            self.user_health_direct_dmg = True
        else:
            self.user_health_direct_dmg = False
