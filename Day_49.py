# Before seeing this code, first you have to know the code of Day 48 
# Day_48.py -> https://github.com/Karanshukl/Replitt-100-days-of-Python-Code-/blob/main/Day_48.py

RED = "\033[032m"
BLUE = "\033[031m"
END="\033[0m"

def highScore_leader():
  print("Analyzing the scores.....")
  print()
  with open("filenames.txt", "r") as f:
    scores = f.read().split("\n")

  highScore = 0
  name = None

  for item in scores:
    data = item.split(">")
    if data != []:
      if int(data[1]) > highScore:
        highScore = int(data[1])
        name = data[0]
        
  print("Current HighScorer is {0}{1}{2} with score {3}{4}{5}".format(RED,name,END,BLUE,highScore,END))  
  
highScore_leader()
