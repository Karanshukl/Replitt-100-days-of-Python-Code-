list = []

try:
  f.open("order.txt", )
  list = eval(f.read())
  f.close()
except Exception as e:
  print(e)

def loadfile():
  with open("order.txt", "w") as f:
    f.write(str(list))
  
def addOrder():
  print()
  name = input("What's your name: ")
  pizza = input("What type of pizza you want (veg or non-veg): ")
  toppings = input("Toppings (Mushroom, Tomato, Panner, Corn, Onion): ")
  try:
    quantity = int(input("How many pizzas you want: "))
  except Exception as e:
    print(e)
    quantity = int(input("How many pizzas you want: "))

  cost = int()
  size = input("Size (Small, Medium, Large): ").capitalize()
  if size == "Small":
    cost = 69
  elif size == "Medium":
    cost = 189
  elif size == "Large":
    cost = 299
  else:
    print(f"Sorry this {size} size is not available")

  total = cost * quantity 
  row = [name,pizza,toppings,quantity,cost,size,total]
  list.append(row)
  loadfile()
  
  
def viewOrder():
  print()
  print(f"{'Name'} {'Pizza':^15} {'Toppings':^15} {'Quantity':^15} {'Cost':^15} {'Size':^15} {'Total':^15}")
  for row in list:
    print(f"{row[0]} {row[1]:^15} {row[2]:^15} {row[3]:^15} {row[4]:^15} {row[5]:^15} {row[6]:^15}")
    print()


while True:
  menu  = input("1: Add Order\n2: View Order\n> ")
  if menu == "1":
      addOrder()
  elif menu == "2":
      viewOrder()
