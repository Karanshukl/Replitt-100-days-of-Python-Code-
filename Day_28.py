import random, os, time as t

print("---------- EPIC 1V1 BATTLE ----------")
print()

def rollDice(side):
  result = random.randint(1,side)
  return result

def health():
  healthStat = ((rollDice(6)*rollDice(12))/2)+10
  return healthStat

def strength():
  strengthStat = ((rollDice(6)*rollDice(8))/2)+12
  return strengthStat

print()
c1Name = input("My SuperHero >> ")
c1Type = input("Type character (Human, Alien, Monster, Animal, Robot or etc.) >> ")
print()
c1Health = health()
c1Strength = strength()
print("My SuperHero Health is", c1Health)
print("My SuperHero Strength is", c1Strength)
print()
print("Who is gonna fight with my superHero")
print()

c2Name = input("Who is your SuperHero >> ")
c2Type = input("Type character (Human, Alien, Monster, Animal, Robot or etc.) >> ")
print()
c2Health = health()
c2Strength = strength()
print("Your SuperHero Health is", c2Health)
print("Your SuperHero Strength is", c2Strength)
print()

round = 1
winner = None

while True:
  t.sleep(1)
  os.system("clear")
  print()


  c1Dice = rollDice(6)
  c2Dice = rollDice(6)

  difference = abs(c1Strength - c2Strength) + 1
  print(f"----------------- Round {round} ---------------------")
  print()
  if c1Dice > c2Dice:
    c2Health -= difference
    if round==1:
      print(c1Name, "wins the first Boom")
    else:
      print(c1Name,"wins", round, "round")
  elif c2Dice > c1Dice:
    c1Health -= difference
    if round==1:
      print(c2Name, "wins the first Bo0m")
    else:
      print(c2Name, "wins", round, "round")
 
  print()
  print(c1Name)
  print("My SuperHero Health is ", c1Health)
  print()
  print(c2Name)
  print("Your SuperHero Health is ", c2Health)
  print()

  if c1Health<=0:
    print(c1Name, "Your SuperHero has died!")
    winner = c2Name
    break
  elif c2Health<=0:
    print(c2Name, "My SuperHero has died!")
    winner = c1Name
    break
  else:
    round += 1
    

t.sleep(1)
os.system("clear")
print()
print("-------------- HORRAH -------------")
print()
print("\033[32m", winner, 'has won in', round, 'rounds' "\033[32m" )
