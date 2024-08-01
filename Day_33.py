# Easy way to make a "To Do  List". If you want some pro-level type of code in this project ping me 
TaskList = []

def doList():
  while True:
    for tasks in TaskList:
      print(tasks)
    print()
    user = input("What do you want to do? (view, add, edit, or quit): ")
    if user == "view":
      print(TaskList)
      print()

    elif user == "add":
      task = input("What task do you want to add: ")
      TaskList.append(task)
      print()

    elif user == "edit":
      task = input("What task do you want to edit: ")
      if task in TaskList:
        TaskList.remove(task)
        
      else:
        print(f"Task '{task}' not found in the list.")
        exit()
        
    elif user == "quit":
      print("Goodbye!")
      break

    else:
      print("Invalid input. Please try again.")
      continue

doList()
