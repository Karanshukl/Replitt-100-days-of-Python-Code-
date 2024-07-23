import random

print("Guessing Game")
print("--------------->")
print()
def guessingGame():
    randomNumber = random.randint(1,10)
    guesses = 0
    while True:
      guess = int(input("Enter your guess number: "))
      if guess == randomNumber:
       print("You win! The number was " + str(guess))
       break
      elif guess <= 0:
        print(f"Negative number or zero not allowed ({guess})")
        exit()
      elif guess > randomNumber:
        print(f"You're guessing too High {guess} ")
        guesses +=1
        print()
      elif guess < randomNumber:
        print(f"You're guessing too Low {guess}")
        guesses +=1
        print()
      else:
        print("Invalid Input")
        exit()
    print()
    print(f"You took {guesses} guesses for the correct number 🏆")


guessingGame()
