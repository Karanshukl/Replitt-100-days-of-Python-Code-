# "Guess the Number" --
print("Guess the Number - Version 1.0")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print()
print("Let's play")

guesses = 0
number = 555

while True:
  guess = int(input("Guess the number:  "))
  if guess < number:
    print("Too low")
    guesses += 1
  elif(guess > number):
    print("Too high")
    guesses += 1
  elif(guess == number):
    print("You got it ✅ ")
    guesses += 1
    break
  elif(guess < 0):
    print("You broke the game")
    exit()
  else:
    print("I don't recognize this number")
    
print(f"You guess the number {number} in {guesses} guesses")    
     

