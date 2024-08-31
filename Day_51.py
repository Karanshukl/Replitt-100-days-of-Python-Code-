import os, time as t

list = []
with open("list.txt", "r") as f:
    list = eval(f.read())

def add():
  add = input("What you want to add: ")
  date = input("Due date: ")
  priority = input("priority: ")
  row = [add,date,priority]
  list.append(row)

def view():
  print("")
  view = "all"
  view = input("""1. View all
2. Sort priority
: """).capitalize()
  print()
  if view == "1" or "view all".lower():
    for row in list:
      print("-".join(row))
  elif view == "2" or "sort priority".lower():  
    for row in list:
      if view[2] == "priority":
       print(", ".join(row))

def remove():
  removeData = input("What you want to remove: ")
  for row in list:
    if removeData in row:
      list.remove(row)
      print("Data Delete sucessfully")

def edit():
  editData = input("What you want to edit: ")
  for task in list:
    if editData in task[0]:
        print(f"Editing task: {task}")
        edit_choice = input("What would you like to edit (add, date, priority)? ")
        if edit_choice == "add":
            new_task_add = input("Enter the new task: ")
            task[0] = new_task_add
        elif edit_choice == "date":
            new_data = input("Enter the new hour: ")
            task[1] = new_data
        elif edit_choice == "priority":
            new_priority = input("Enter the new priority: ")
            task[2] = new_priority
        else:
            print("task hour or prio")
        print("Task updated successfully.")
        print("")
        break
  else:
    print(f"Task '{editData}' not found in the to-do list.")

menu = "e".lower
while menu != "e": 
        print(" >>>>  ToDo List <<<<")
        menu = input("""
1. add
2. view
3. edit
4. remove

: """)
        menu = menu.strip().lower()
        if menu == "1" or menu == "add":
            add()
        elif menu == "2" or menu == "view":
            view()
        elif menu == "3" or menu == "edit":
            edit()
        elif menu == "4" or menu == "remove":
            remove()
        t.sleep(1)
        os.system("clear")
        with open("list.txt", "+w") as f:
            f.writelines(str(list))
