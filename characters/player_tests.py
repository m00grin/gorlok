class Player:
  def __init__(self, name, initial_hp):
    self.name = name
    self.hp = initial_hp
  def attack(self, enemy, dmg):
    print(f"{self.name} attacks {enemy.name}!")
    enemy.hp -= dmg

class Enemy:
  def __init__(self, name):
    self.name = name
    self.hp = 100
  def attack(self, player, dmg):
    print(f"{self.name} attacks {player.name}!")
    player.hp -= dmg

class Game:
  def __init__(self, player_name, enemy_name, initial_hp, player_dmg, enemy_dmg):
    self.player = Player(player_name, initial_hp)
    self.enemy = Enemy(enemy_name)
    self.player_dmg = player_dmg
    self.enemy_dmg = enemy_dmg

  def game_loop(self):
    while True:
      self.player.attack(self.enemy, self.player_dmg)
      self.enemy.attack(self.player, self.enemy_dmg)
      if self.player.hp <= 0 and self.enemy.hp <= 0:
        print('you killed eachother. gj idiot')
        break
      if self.player.hp <= 0:
        print("you lose")
        break
      if self.enemy.hp <= 0:
        print("enemy loses")
        break
    print('out')

name = input('Who is playing this? ')
enemy_name = input('Who are you fighting? ')
game = Game(name, enemy_name, 100, 10, 10)


game2 = Game(name, enemy_name, 200, 30, 20)

# game.game_loop()
game2.game_loop()
