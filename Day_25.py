# If you have any questions regarding any programming problems give me a comment

def rollDice(sides):
   import random
   result = random.randint(1,sides)
   return result

def roll_6_and_8():
    roll_6dice = rollDice(6)
    roll_8dice = rollDice(8)
    health = roll_6dice * roll_8dice   
    return health

print("⚔️  Superhero stats generator ⚔️")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()

Character = "yes"
while Character == "yes":
     superhero = input("Name your Superhero: ")
     health = str(roll_6_and_8())                             
     print(f'Your {superhero} health is >> {health} HP')
     print()
     Character = input("want to check another Superhero health:  ")






