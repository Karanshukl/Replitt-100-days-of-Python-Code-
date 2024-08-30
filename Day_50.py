import random 

def add_ideas():
  with open("myIdeas.txt", "a+") as f:
    user = input("Enter your Idea: ")
    data = f.write(f"{user}\n")
  

def read_ideas():
  with open("myIdeas.txt", ) as f:
    read = f.readlines()
    random_read = random.choice(read)
    print(random_read)

while True:
  menu = input("1. add: 2. show:")
  if menu == "1":
    add_ideas()
  elif menu == "2":
    read_ideas()
  else:
    break
    
