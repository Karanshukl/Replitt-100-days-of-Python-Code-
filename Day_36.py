namelist = []

def printList():
  print()
  for name in namelist:
    print("\033[34m"f"{name}""\033[37m")
    print()
  print()

while True:
  fName = input("\033[32m""Enter your first name: ").strip().capitalize()
  lName = input("\033[32m""Enter your last name: ").strip().capitalize()
  name = f"{fName}  {lName}"
  
  if name not in namelist:
    namelist.append(name)
  elif name in namelist:
    print()
    print("\033[31m"f"{name} is already in list.""\033[31m")
    exit()
  else:
    print("Error: This is not a valid Syntex")
    break
    
  printList()
 
