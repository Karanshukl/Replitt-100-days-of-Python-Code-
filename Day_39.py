import random

listOfWords = ["python", "coder", "developer", "ds"]
letterPicked = []
lives = 6

word = random.choice(listOfWords)

while True:
  letter = input("Choose a letter: ").lower()
  
  if letter in letterPicked:
    print("You've tried that before")
    print()
    continue
    
  letterPicked.append(letter)
  
  if letter in word:
    print("You found a letter")
    break
  else:
    print("Nope, not in there")
    lives -= 1

  if lives<=0:
    print(f"You ran out of lives! The answer was {word}")
    break
  else:
    print(f"Only {lives} left")
    print()
