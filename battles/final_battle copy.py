# final battle component of Gorlok game

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import time
import subprocess
from characters.enemies import gorlok
from characters.player import player
from weapons import melee

def run_battle():
    # Final battle sequence
    
    enemy = gorlok()

    print(f"\n{enemy.name} has {enemy.hp} hitpoints.")
    print("...")
    print("He sneers at you and blows green snot from his nose.")
    print("...")

run_battle()

#     while enemy_hp > 0:
#         atk_1 = input(f"Do you want to swing your enchanted sword at {enemy_name}? ").strip().lower()
    
#         if atk_1 == "yes":
#             enchanted_dmg = enchanted_sw
# ord(sword_dmg, enchant_str, weapon_cond, enemy_armor)
#             enemy_hp -= int(enchanted_dmg)
#             weapon_cond -= .01
#             enemy_armor -= .05
#             print("...")
#             print(f"The enchanted sword does {int(enchanted_dmg)} damage to {enemy_name}!")
#             print("...")
#             if enemy_hp == 1:
#                 print(f"{enemy_name} now has {enemy_hp} hitpoint.")
#                 print("...")
#             else:
#                 print(f"{enemy_name} now has {enemy_hp} hitpoints.")
#                 print("...")
#         elif atk_1 == "no":
#             print("...")
#             print(f"{enemy_name} kills you.")
#             print("Womp womp.")
#             print("...")
#             print("Game over.")

#             while True:
#                 again = input("Try again? (yes/no): ").strip().lower()
#                 if again == "yes":
#                     subprocess.run(["python", "gorlok.py"])
#                     break
#                 elif again == "no":
#                     print("...")
#                     print("Coward. Game over.")
#                     exit()
#                     break
#                 else:
#                     print("...")
#                     print("Huh?\n")
#                     continue
#         else:
#             print("...")
#             print(f"It's a 'yes' or 'no' moment, friend. {enemy_name} is impatient and unimpressed, but still alive.")
#             print("...")
    
#         if enemy_hp <= 0:
#             print("...")
#             print(f"You kicked {enemy_name}'s ass. He's dead dead.")
#             break

#         if enemy_hp < 50 and enemy_hp > 0:
#             enemy_hp = int(enemy_hp * 1.03)
#             if enemy_hp == 1:
#                 print(f"{enemy_name} sips dat sweet, sweet health potion. He now has {int(enemy_hp)} hitpoint.")
#             else:
#                 print(f"{enemy_name} sips dat sweet, sweet health potion. He now has {int(enemy_hp)} hitpoints.")
#                 print("...")
#     if enemy_hp <= 0:
#         print("...")
#         print(f"{enemy_name}'s family gathers around his motionless corpse.")
#         print("...")
#         newgame = input("Start new game? ")
#         if newgame == "yes":
#             subprocess.run(["python", "gorlok.py"])
#         else:
#             print("\nYou scared-ass bitch!")
#             print("\nGame over..")
#             exit()

# if __name__ == "__main__":
#     run_battle()