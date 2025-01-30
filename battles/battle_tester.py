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
from battles import battle_end_victory

def test_battle():

    enemy = gorlok()
    player_instance = player()


    print(f"\n{enemy.name} has {int(enemy.hp)} hit points.")

    atk_1 = input(f"Do you want to swing your {player_instance.weapon().name} at {enemy.name}? ").strip().lower()


    if atk_1 == "yes":
        damage = player_instance.weapon().damage  # Get the player's weapon damage
        print(f"{player_instance.weapon().name} does {int(damage)} damage to {enemy.name}!")
        
        # Apply damage to enemy
        actual_damage = enemy.take_damage(damage)
        print(f"{enemy.name} now has {int(enemy.hp)} hit points left after taking {int(actual_damage)} damage.")
        
        # Check if enemy is still alive
        if enemy.hp <= 0:
            print(f"{enemy.name} has been defeated!")
            print(f"\n{enemy.name}'s family gathers around his motionless corpse.")
            exit()
        else:
            atk_2 = input(f"Do you want to swing your {player_instance.weapon().name} at {enemy.name} again? ").strip().lower()
            damage = player_instance.weapon().damage  # Get the player's weapon damage
            print(f"{player_instance.weapon().name} does {int(damage)} damage to {enemy.name}!")
        
            # Apply damage to enemy
            actual_damage = enemy.take_damage(damage)
            print(f"{enemy.name} now has {int(enemy.hp)} hit points left after taking {int(actual_damage)} damage.")
        
            # Check if enemy is still alive
        if enemy.hp <= 0:
            # battle_end_victory()
            print(f"{enemy.name} has been defeated!")
            print(f"\n{enemy.name}'s family gathers around his motionless corpse.")
            exit()
        else:
            atk_3 = input(f"Do you want to swing your {player_instance.weapon().name} at {enemy.name} again? ").strip().lower()
            damage = player_instance.weapon().damage  # Get the player's weapon damage
            print(f"{player_instance.weapon().name} does {int(damage)} damage to {enemy.name}!")
        
            # Apply damage to enemy
            actual_damage = enemy.take_damage(damage)
            print(f"{enemy.name} now has {int(enemy.hp)} hit points left after taking {int(actual_damage)} damage.")
        
            # Check if enemy is still alive
        if enemy.hp <= 0:
            print(f"{enemy.name} has been defeated!")
            print(f"\n{enemy.name}'s family gathers around his motionless corpse.")
            exit()
        else:
            print(f"{enemy.name} is bored with your bullshit and flies away into the night sky.")
                    
# Call the battle function to start the test
# test_battle()