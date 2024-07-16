# Generation Generator --
print("Generation Generator")
print("~~~~~~~~~~~~~~~~~~~~~~")
generate = int(input("Enter the year you were born: "))
if ((generate >= 1925) and (generate <= 1946)):
  print ("Traditionalists")
elif ((generate >= 1947) and (generate <= 1964)):
  print ("Baby Boomers")
elif ((generate >= 1965) and (generate <= 1981)):
  print ("Generation X")
elif ((generate >= 1982) and (generate <= 1995)):
  print ("Millenials")
elif ((generate >= 1996) and (generate <= 2015)):
  print ("Generation Z ")
else:
  print("You are not in any Generation")

