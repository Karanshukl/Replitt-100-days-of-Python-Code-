print("MATH GAME 🕹️")
print()
number  = int(input("Name of your multiples: "))
print()

score = 0
for i in range (1, 11):
  round = i* number
  answer = int(input(f"{number} * {i} = "))
  if round == answer:
    score += 1
    print("Nice 👌")  
  else:
    print(f"Wrong :> Answer was {round}")

print()
print("------------------------------")
print(f"You scored {score} out of 10")
print()
if score == 10:
  print("You're a genius 🤓")
elif score >= 7:
  print("You're Good 👍")
else:
  print("You've to improve yourself 🥲 ")




