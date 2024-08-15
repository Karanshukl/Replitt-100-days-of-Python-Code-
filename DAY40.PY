
print("---------- 💳 CONTACT CARD 💳 ----------")
print()

def Contact():
  name = {"Enter your name": "Hradesh"}
  print(f"Name: {name['Enter your name']}")
  
  DOB = {"Enter your D.O.B": "23/033/2002"}
  print(f"DOB: {DOB['Enter your D.O.B']}")
  
  TelNo = {"Enter your telephone number": 4655852}
  print(f"Telehone Number: {TelNo['Enter your telephone number']}")
  
  Email = {"Enter your E-mail": "iloveubunto@gmail.com"}
  print(f"E-mail: {Email['Enter your E-mail']}")
  
  Address = {"Country": "India"}
  print(f"Address: {Address['Country']}")
  print()
  
  print(f"""Hi \033[32m{name['Enter your name']}.\033[0m Our dictionary says that you were born on \033[34m{DOB['Enter your D.O.B']},\033[0m we call you on \033[33m{TelNo['Enter your telephone number']},\033[0m email \033[31m{Email['Enter your E-mail']},\033[0m or write to the Cupboard Under the Stairs, Replit Towers, NY.""")
  
Contact()
