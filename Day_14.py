from getpass import getpass as input
print(" E P I C  🪨  📄 ✂️    B A T T L E ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("""Rules :>
~~~~~~~~~~~~~~~~~~~~~
Rock beats Scissors, Scissors beats Paper & Paper beats Rock

R for Rock 
S for Scissors 
P for Paper
""")
print("Enter your turn Player1: ")
player1 = input("")
print("Enter your turn Player2: ")
player2 = input("")
if (player1 == player2):
  print("Match Draw 📍")
elif ((player1 == "R") and (player2 == "S")):
  print(f"PLayer 1 is Win {player1} 🪨")
elif ((player1 == "S") and (player2 == "P")):
  print(f"PLayer 1 is Win {player1} ✂️")
elif ((player1 == "P") and (player2 == "R")):
  print(f"PLayer 1 is Win {player1} 📄")
elif ((player1 == "S") and (player2 == "R")):
  print(f"PLayer 2 is Win {player2} ✂️")
elif ((player1 == "P") and (player2 == "S")):
  print(f"PLayer 2 is Win {player2} 📄")
elif ((player1 == "R") and (player2 == "P")):
  print(f"PLayer 2 is Win {player2} 🪨")
else:
  print("Invalid Input")


