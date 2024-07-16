# How many seconds are in a year --
print("How many seconds are in a year? ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Is it a leap year?")
year = input()
if year == "Yes" or year == "yes":
  seconds = 366*24*60*60
  print("A leap year has:",seconds, "seconds")
elif year == "No" or year == "no":
  seconds = 365*24*60*60
  print("A year has:",seconds, "seconds")
else:
  print("Enter Yes or No")

