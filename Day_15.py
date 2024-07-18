# Ask the user what animal sound they want to hear -- 
print("what animal sound they want to hear? ")
exit = "no"

while exit == "no":
  animal =  input("What animal do you want hear: ")
  if animal == "cow":
    print("🐮 moo")
  elif animal ==  "dog":
    print("🐶 wof wof")
  elif animal ==  "cat":
    print("🐱 meww meww")
  elif animal ==  "lion":
    print("🦁 roarrr")
  else:
    print("I don't know this animal sound 😁")

  exit = input("Exit: ")
