import random, os, time 

def rollDice(sides):
  result = random.randint(1, sides)         # For random number 
  return result

def healthStats():
  sixdiceroll = random.randint(1,6)
  eightdiceroll = random.randint(1,12)
  healthStats = (sixdiceroll * eightdiceroll / 2) + 10 
  return healthStats

def strengthstats():
  sixdiceroll = random.randint(1,6)
  eightdiceroll = random.randint(1,12)
  strengthstats = (sixdiceroll * eightdiceroll / 2) + 12 
  return strengthstats


while True:
 print("Character Builder Game 🎮")
 print()
 name = input('Name your SuperHero >> ')
 type = input('Character type (Human, Alien, Monster, Animal, Robot or etc. >> ')
 print()
 print(f"Your SuperHero Health Stats: {healthStats()} ")
 print(f"Your SuperHero Strength stats: {strengthstats()} ")
 print()
 print("May your name go down in Legend…")
 print()
 Again = input("You want to Create another SuperHero: ")
 print()
 Again = Again.lower()
 if Again == "yes":
   time.sleep(1)
   os.system("clear")
 else:
     exit()
