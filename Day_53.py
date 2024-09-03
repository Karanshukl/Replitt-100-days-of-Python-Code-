inventory = []

try:
  with open("game.txt", ) as f:
    list = eval(f.read())
except Exception as e:
  print(e)
    
def add():
  item = input("What you want to Add: ").capitalize()
  inventory.append(item)
  print("Added Succesfully!")

def view():
  printed_items = set()
  for item in inventory:
      if item not in printed_items:
          count = inventory.count(item)
          print(f"{item}:{count}")
          printed_items.add(item)
          
  
def remove():
  item = input("What do you want to remove: ").capitalize()
  if item in inventory:
      inventory.remove(item)
      print("removed Succesfully!")
def updateFile():
  f = open("Inventory.txt","w")
  f.write(str(inventory))
  f.close()
      

playing = True
while playing:
  option = int(input("""
  1. Add
  2. View
  3. Remove
  :> """))
  if option == 1:
    add()
  elif option == 2:
    view()
  elif option == 3:
    remove()
  else:
    print("Invalid input: Choose (1 or 2 or 3)")
    continue
    
  
