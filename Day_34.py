import os, time as t

mailList = []

def mailcheck ():
  os.system("clear")
  print()
  counter = 1
  for mail in mailList:
    print(f"{counter}: {mail}")
    counter += 1
  print()
  t.sleep(1)

def spam(time):
  for i in range(0, time):
    print(f"""Email  {i+1}
    
Dear {mailList[i]}
It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.

Love and hugs,
Ian Spammington III
    """)
    t.sleep(1)
    os.system("clear")
  

while True:
  print(" 1: Add mail\n 2: Show mail\n 3: Remove mail\n 4:Get Spamming")
  user = int(input(" Chose your number (1-4): "))
  if user == 1:
    mail = input(" Add Email here: ")
    mailList.append(mail)
   
  elif user == 2:
    mailcheck()

  elif user == 3:
    mail = input(" Remove Email: ")
    if mail in mailList:
      mailList.remove(mail)
    else:
      print(f" Your {mail} is not in list ")

  elif user == 4:
    spam(10)
  t.sleep(1)
  os.system("clear")
  
    


    
  
  










  
    

    
