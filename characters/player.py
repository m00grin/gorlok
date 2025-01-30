# player stats and attributes

from weapons.melee import rusty_spoon

class player:
    def __init__(self):
        self.name = "Player"
        self.hp = 100
        self.armor = None
        self.weapon = rusty_spoon