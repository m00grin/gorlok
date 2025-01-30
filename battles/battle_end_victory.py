# Winning battle end sequence

import sys
import time
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from characters.enemies import gorlok
from characters import player

def battle_won():
    enemy = gorlok()
    print("\n")
    print(f"\033[1;31m- Congratulations! You have defeated {enemy.name}! -\033[0m")
    print()
    exit()
    return