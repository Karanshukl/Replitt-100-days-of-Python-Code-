import datetime

today = datetime.date.today()
user = input("What event are you waiting for: \n")

day= int(input())
month=int(input())
year=int(input())
data = datetime.date(year,month,day)
diff = abs(today-data)
diff = diff.days

if data == today:
  print("Party 🎉")
elif data < today:
  print(f"We missed your {user}😳")
elif data > today:
  print(f"{diff} Days left 🥳")
else:
  print("Invalid input")
