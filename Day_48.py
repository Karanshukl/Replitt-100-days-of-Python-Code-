import random

def high_score_table():
  print("❌ HIGH SCORE TABLE ✖️")
  print()
  while True:
    input1 = input("Enter your Initials: ")
    score = random.randint(1,1000000)
    print()

    with open("highScore.txt", "a") as f:
      f.write(f"{input1} > {score}\n")

    print("Added to high score table")
    addMore = input("Add More (Y/N) ? ").capitalize()
    print()
    if addMore == "Y":
      continue
    elif addMore == "N":
      exit()
    else:
      print("Invalid input ")
      print()
      continue
            
high_score_table()
