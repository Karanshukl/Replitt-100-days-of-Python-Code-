class character:
  def __init__(self, name, health,magicPoints):
    self.name =  name 
    self.health = health
    self.magicPoints = magicPoints

  def prettyPrint(self):
    print(f"""Name: {self.name}
Health: {self.health}
Magic Points: {self.magicPoints}
    """)

class player(character):
  def playerDetails (self, name, health, magicPoints, lives, alive):
    super().__init__(name, health, magicPoints)
    self.lives = lives
    self.alive  = alive

  def prettyPrint(self):
     print("Player")
     print(f"""Name: {self.name}
Health: {self.health}
Magic Points: {self.magicPoints}
Lives: {self.lives}
Alive: {self.alive}
     """)

  def isAlive(self):
    if self.alive > 0:
      print("Lives Available")

    else:
      print("You're out of lives")


class enemy(character):
  def enemyDetails(self, name, health, magicPoints, type, strength):
     super().__init__(name, health, magicPoints)
     self.type = type
     self.strength = strength 

  def prettyPrint(self):
     print(f"""Name: {self.name}
Health: {self.health}
Magic Points: {self.magicPoints}
Type: {self.type}
Strength: {self.strength}
     """)

class orc(enemy):
  def orcDetails(self, name, health, magicPoints, type, strength, speed):
     super().enemyDetails(name, health, magicPoints, type, strength)
     self.speed = speed

  def prettyPrint(self):
     print(f"""Name: {self.name}
Health: {self.health}
Magic Points: {self.magicPoints}
\033[31mType: {self.type}\033[0m
Strength: {self.strength}
Speed: {self.speed}
     """)
    
class vampire(enemy):
  def vampireDetails(self, name, health, magicPoints, type, strength, speed, dayNight):
     super().enemyDetails(name, health, magicPoints, type, strength)
     self.speed = speed
     self.dayNight = dayNight

  def prettyPrint(self):
     print(f"""Name: {self.name}
Health: {self.health}
Magic Points: {self.magicPoints}
\033[34mType: {self.type}\033[0m
Strength: {self.strength}
Speed: {self.speed}
Day or Night: {self.dayNight}
     """)
    

def main():
  # player
  player1 = player("Carlos", 96, 50)
  player1.playerDetails("Carlos", 96, 50, 4, "yes")


  # Vampires
  vampire1 = vampire("Dracula", 120, 80)
  vampire1.vampireDetails("Dracula", 120, 80, "Vampire", 75, 30, "Night")

  vampire2 = vampire("Nosferatu", 110, 85)
  vampire2.vampireDetails("Nosferatu", 110, 85, "Vampire", 70, 25, "Night")

  # Orcs
  orc1 = orc("Gruk", 150, 30)
  orc1.orcDetails("Gruk", 150, 30, "Orc", 90, 20)

  orc2 = orc("Throk", 140, 35)
  orc2.orcDetails("Throk", 140, 35, "Orc", 85, 18)

  orc3 = orc("Mogor", 130, 40)
  orc3.orcDetails("Mogor", 130, 40, "Orc", 80, 22)

  # Display details
  player1.prettyPrint()
  vampire1.prettyPrint()
  vampire2.prettyPrint()
  orc1.prettyPrint()
  orc2.prettyPrint()
  orc3.prettyPrint()

if __name__ == '__main__':
   main()

