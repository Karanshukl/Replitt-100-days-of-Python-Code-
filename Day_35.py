import os, time as t

todolist = []
def List():
  print()
  counter = 0
  for items in todolist:
    counter +=1
    print(f'{counter} : {items}')
  print()

while True:
  print()
  menu = input("What you wanna do view, add or remove : ")
  if menu == "view":
    List()
  elif menu == 'add':
    item = input("Add here: ").title()
    todolist.append(item)
    
  elif menu == "remove":
    item = input("what you want to remove: ").title()
    check = input("Are you sure you want to remove this?\n")
    if check.startswith ("y"):
      if item in todolist:
       todolist.remove(item)
       print(f"Now {item} is not in the list")
  else: 
    print(f"This {menu} is Unknown")
  
  t.sleep(2)
  os.system("cls")


  
