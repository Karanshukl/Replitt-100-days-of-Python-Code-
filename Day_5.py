# Common errors 
myName = input("What's your name?: ")
if myName == "David":
  print("Hii Buddy")      #Here you've to add print funtion

# Syntax Error
catsOrDogs = input("Are you a cat person? Or a dog person?: ")
if (catsOrDogs == "cat"):  #you've to add (==) for comparison              
  print("Meow")
else:
  print("Woof")

# Syntax Error
catsOrDogs = input("Are you a cat person? Or a dog person?: ")
if (catsOrDogs == "cat"):   #You've to add (:) colon here 
  print("Meow")
else:
  print("Woof")

# Indentation Error
catsOrDogs = input("Are you a cat person? Or a dog person?: ")
if catsOrDogs == "cat":
  print("Meow")
else:
 print("Woof")       #Add Indentation here 

# Multiple errors
drink = input("Do you prefer coffee or tea?")   #Add Double prime (") here, after coffee and tea?"
if (drink == "coffee"):        #Add (==)
  print("Tea is better.")
else:                           #Add Indentation here 
  print("Excellent choice.")






#"Which character are you?" Generator --

print("Fast & Furious moive character creator --  ", sep=" ")

Dom = input("Are you a 'good leader'? ")
if (Dom == "yes"):
  print("Dom is one of the best leader in the world ❤️", sep=" ")
elif (Dom == "no"):
  print("You're not a good leader", sep=" ")

Brian = input("Can you drive a car in 'Extreme level'? ")
if (Brian == "yes"):
  print("You're Brian O'Conner 🏎️", sep=" ")
elif (Brian == "no"):
  print("You're not Brian O'Conner")

LukeHobbs = input("Are you a 'Cop'? ")
if (LukeHobbs == "yes"):
  print("You're best Cop 👮‍♂️", sep=" ")
elif (LukeHobbs == "no"):
  print("You're not Luke Hobbs", sep=" ")

if (Dom == "no" and Brian == "no" and LukeHobbs == "no"):
  print("You're not a Fast & Furious character")

elif ((Dom != "yes" and Dom != "no") and (Brian != "yes" and Brian != "no") and (LukeHobbs != "yes" and LukeHobbs != "no")):
  print("You Have to answer yes or no")

        
