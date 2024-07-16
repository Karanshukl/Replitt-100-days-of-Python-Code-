
# Common Errors --
tvShow = input("What is your favorite tv show? ")
if tvShow == "peppa pig":
  print("Ugh, why?")
elif tvShow == "paw patrol":
  print("Aww, sad times")
elif ((tvShow != "paw patrol") and (tvShow != "peepa pig")):
  print("Chose paw patrol or peepa pig")
else:
 print("Yeah, that's cool and all…")

faveCharacter = input("Who is your favorite character? ")
  
if faveCharacter == "daddy pig":
    print("Right answer")
else:
    print("Nah, Daddy Pig's the greatest")


# FIx my code --
tvShow = input("What is your favourite tv show? ")
if tvShow == "peppa pig":
  print("Ugh, why?")
elif tvShow == "paw patrol":
 print("Aww, sad times")
else:
 print("Yeah, that's cool and all…")

faveCharacter = input("Who is your favourite character? ")
if faveCharacter == "daddy pig":
  print("Right answer")
else:
 print("Nah, Daddy Pig's the greatest")


# Fix my code --
order = input("What would you like to order: pizza or hamburger? ")

if order == "hamburger":
  print("Thank you.")
elif order == "pizza":
  print("Pizza coming up.")
  
cheese = input("Do you want cheese?")
if cheese == "yes":
  print("You got it.")
else: 
    print("No cheese it is.")

toppings = input("Do you want pepperoni on that?")
if toppings == "yes":
    print("We will add pepperoni.")
else:
  print("Your pizza will not have pepperoni.")


# Fake Fan Question Generator
print("Hello there!")
print("Do you know programming language? ")
Answer = input()
print("................")
if Answer == "yes":
    print("Which one?")
    language = input()
    if language == "python":
        print("Great, let me know a mapping data type in Python: ")
        Datatypes = input()
        if ((Datatypes == "dict") or (Datatypes == "dictionary")):
            print("You're right!")
        else:
            print("I don't think you know any Datatypes")
    elif (language == "javascript"):
      print("Nice, Can we use Javascript for Web Development? ")
      answer = input("")
      if (answer == "yes"):
       print ("You're right ")
      elif (answer == "may be"):
       print("Go and Learn the Basics")
      else:
        print("You're wrong")
        
else:
    print("You should learn at least one progrmming language!")

