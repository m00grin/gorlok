# simple fighting game test

def enchanted_sword(sword_dmg, enchant_str, weapon_cond, enemy_armor):
    enchanted_dmg = sword_dmg + enchant_str * weapon_cond
    new_enchanted_dmg = enchanted_dmg * enemy_armor
    return new_enchanted_dmg

while True:

    enemy_name = "Gorlok"
    enemy_hp = 100
    sword_dmg = 20
    enchant_str = 2
    weapon_cond = 1
    enemy_armor = 1

    print(f"{enemy_name} has {enemy_hp} hitpoints.")
    print("...")
    print("He sneers at you and blows green snot from his nose.")
    print("...")

    while enemy_hp >0:
        atk_1 = input(f"Do you want to swing your enchanted sword at {enemy_name}? ").strip().lower()
    
        if atk_1 == "yes":
            enchanted_dmg = enchanted_sword(sword_dmg, enchant_str, weapon_cond, enemy_armor)
            enemy_hp -= int(enchanted_dmg)
            weapon_cond -= .01
            enemy_armor -= .05
            print("...")
            print(f"The enchanted sword does {int(enchanted_dmg)} damage to {enemy_name}!")
            print("...")
            if enemy_hp == 1:
                print(f"{enemy_name} now has {enemy_hp} hitpoint.")
                print("...")
            else:
                print(f"{enemy_name} now has {enemy_hp} hitpoints.")
                print("...")
        elif atk_1 == "no":
            print("...")
            print(f"{enemy_name} kills you.")
            print("Womp womp.")
            print("...")
            again = input("Go again? ")
            if again == "yes":
                break
            else:
                print("...")
                print("Coward. Game over.")
                exit()
        else:
            print("...")
            print(f"It's a 'yes' or 'no' moment, friend. {enemy_name} is impatient and unimpressed, but still alive.")
            print("...")
    
        if enemy_hp <= 0:
            print("...")
            print(f"You kicked {enemy_name}'s ass. He's dead dead.")
            break

        if enemy_hp < 50 and enemy_hp > 0:
            enemy_hp = int(enemy_hp *1.03)
            if enemy_hp == 1:
                print(f"{enemy_name} sips dat sweet, sweet health potion. He now has {int(enemy_hp)} hitpoint.")
            else:
                print(f"{enemy_name} sips dat sweet, sweet health potion. He now has {int(enemy_hp)} hitpoints.")
                print("...")
    if enemy_hp <= 0:
        print("...")
        print(f"{enemy_name}'s family gathers around his motionless corpse.")
        print("...")
        exit()