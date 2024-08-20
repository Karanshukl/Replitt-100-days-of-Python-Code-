print("👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾")

def mylist():
  mokebeast = {"Name": None,"Type": None, "Move": None, "Strength": None, "Power": None}
  print()
    
  for i  in mokebeast.keys():
    mokebeast[i] = input(f"{i}: ")
    
  if mokebeast["Type"] == "earth":
    print("\033[36m")
  elif mokebeast["Type"] == "fire":
    print("\033[031m")
  elif mokebeast["Type"] == "water":
    print("\033[34m")
  elif mokebeast["Type"] == "air":
    print("\033[37m")

  for i,j in mokebeast.items():
    print(f"{i} --> {j}")
      
mylist()
