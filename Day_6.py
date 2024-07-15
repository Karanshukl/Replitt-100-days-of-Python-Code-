#Add elif statement
print("SECURE LOGIN")
username = input("Username > ")
if username == "mark":
  print("Welcome Mark!")
elif username == "suzanne":
  print("Hey there Suzanne!")
else:
  print("Go away!")

#Add a Password --
print("SECURE LOGIN")
username = input("Username > ")
password = input("Password> ")

if username == "mark" and password == "password":
  print("Welcome Mark!")
elif username == "Su74nne" and password == "Su74nne":
  print("Hey there Suzanne!")
else:
  print("Go away!")

#Common Error --
print("SECURE LOGIN")
username = input("Username > ")

if username == "mark":
  print("Welcome Mark!")
elif username == "suzanne":
  print("Hey there Suzanne!")
else:
 print("Go away!")


#Fix my code -- 
season = input("what is your favorite season?")
if season == "spring":
  print("Ah! The birds are chirping and flowers blooming.")
elif season == "summer":
  print("Catch some sun and cool off with a lemonade.")
elif season == "autumn":
  print("The leaves are changing and the air is crisp. Enjoy!")
elif season == "winter":
  print("Stay warm by the fire and watch the snow fall.")
else: 
 print("I don't know that season. Please try again.")


#Day 6 Challenge --
print("MY LOGIN SYSTEM")

username = input("Username: ")
password = input("Passwprd: ")
print("................")
if (username == "Hradesh Shukla" and password == "User@123"):
  print ("Hello Hradesh Shukla here, How are you?")

elif (username == "You" and password == "You@123"):
  print ("Hi Buddy, What are you Doing?")

elif (username == "Karan" and password == "Pass@123"):
  print ("Hi Karan, What's your Age?")

else:
  print("Who are you?")


