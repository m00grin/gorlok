# Enemy stats and attributes

import sys
import time
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from weapons.melee import nether_axe
from armor.hades_plate import hades_plate

# enemy class

class gorlok:
    def __init__(self):
        self.name = "Gorlok"
        self.hp = 500
        self.armor = hades_plate()
        self.weapon = nether_axe

    # enemy battle mechanics

    def take_damage(self, damage):
        reduced_damage = max(damage - self.armor.defense, 0)
                             
        # Subtract the reduced damage from enemy's health
        self.hp -= reduced_damage
        return reduced_damage