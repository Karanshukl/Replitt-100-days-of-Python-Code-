import random

print("Infinite Dice Game 🎲")
print("========================)")
print()

def rollDice(sides): 
    total = 0       # For countring the total number of rolls
    play = "yes"    
    roll = random.randint(1, sides)    # For random number generation
    print("You rolled", roll)
    total += 1
    while play == "yes":
        print()
        play = input("Do you want to roll again? (yes/no): ")       # Player's choice to play again
        if play == "yes":
            roll = random.randint(1, sides)  
            print("You rolled", roll)  
            total += 1       # Counting total number of roll's
        else:
            print()
            print(f' >>>>> You rolled a dice total of {total} time\'s ')    # For the total number of roll's
            break


sides = int(input("How many sides of dice: "))   # Taking input from the player 
rollDice(sides)    
