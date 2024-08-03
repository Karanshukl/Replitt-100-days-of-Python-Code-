todolist = []
def List():
  print()
  counter = 0
  for item in todolist:
    counter +=1
    print(f'{counter} : {item}')
  print()

while True:
  print()
  menu = input("What you wanna do view, add or remove : ")
  if menu == "view":
    List()
  elif menu == 'add':
    item = input("Add here: ")
    todolist.append(item)
  elif menu == "remove":
    item = input("what you want to remove: ").title()
    check = input("Are you sure you want to remove this?\n")
    if check[0]=="y":
     if item in todolist:
       todolist.remove(item)
  else: 
    print(f"This {menu} is Unknown")

  List()

  
