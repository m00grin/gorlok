# messy space to try battle logic

# imports
import subprocess
import sys
import time
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from characters.enemies import gorlok
from characters.player import player
from weapons.melee import rusty_spoon
from weapons.melee import nether_axe
from armor import hades_plate

def test_battle():

    enemy = gorlok()
    player_instance = player()


    print(f"\n{enemy.name} has {enemy.hp} hitpoints.")

    atk_1 = input(f"Do you want to swing your {player_instance.weapon().name} at {enemy.name}? ").strip().lower()


    if atk_1 == "yes":
        damage = player_instance.weapon().damage  # Get the player's weapon damage
        print(f"{player_instance.weapon().name} does {int(damage)} damage to {enemy.name}!")
        
        # Apply damage to enemy
        actual_damage = enemy.take_damage(damage)
        print(f"{enemy.name} now has {int(enemy.hp)} hitpoints left after taking {int(actual_damage)} damage.")
        
        # Check if enemy is still alive
        if enemy.hp <= 0:
            print(f"{enemy.name} has been defeated!")
        else:
            atk_2 = input(f"Do you want to swing your {player_instance.weapon().name} at {enemy.name} again? ").strip().lower()
            damage = player_instance.weapon().damage  # Get the player's weapon damage
            print(f"{player_instance.weapon().name} does {int(damage)} damage to {enemy.name}!")
        
            # Apply damage to enemy
            actual_damage = enemy.take_damage(damage)
            print(f"{enemy.name} now has {int(enemy.hp)} hitpoints left after taking {actual_damage} damage.")
        
            # Check if enemy is still alive
            if enemy.hp <= 0:
                print(f"{enemy.name} has been defeated!")
            else:
                atk_3 = input(f"Do you want to swing your {player_instance.weapon().name} at {enemy.name} again? ").strip().lower()
            damage = player_instance.weapon().damage  # Get the player's weapon damage
            print(f"{player_instance.weapon().name} does {int(damage)} damage to {enemy.name}!")
        
            # Apply damage to enemy
            actual_damage = enemy.take_damage(damage)
            print(f"{enemy.name} now has {int(enemy.hp)} hitpoints left after taking {actual_damage} damage.")
        
            # Check if enemy is still alive
            if enemy.hp <= 0:
                print(f"{enemy.name} has been defeated!")
            else:
                print(f"{enemy.name} is bored with your bullshit and flies away into the night sky.")
                    
# Call the battle function to start the test
test_battle()