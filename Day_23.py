def login():
  print("Welcome to the login page :)")
  print("------------------------------>")
  print()

  maxAttemps = 4  # Set max attemps for user
  attemps = 0    # Collecting user attemps
  while attemps < maxAttemps:
    username = input("Enter you username: ")
    username = username.lower()    
    password = input("Enter your password: ")
    print()
    if ((username == "Hradesh" or "hradesh") and (password == "admin@123")):
     print("Login succesfull ✅ ")
     break    # Login succesfull out for the loop 
    else:
      attemps += 1  # user attemps collect (Increment)
      if (attemps == maxAttemps):
       print()
       print("\033[31m","Too many attemps: Login failed ❌","\033[31m")    # Exit the loop after exceeding (out of limit) attemps
       exit()
      else:
        print()
        print(f"Invalid username ({username}) or password ({password}): Try again ⚠️ ")    
        print("You have", maxAttemps - attemps ,"attemps left")
        print()


login()   




# If you find helpful drop a comment 
