# Grade Generator --
print("Grade Generator")
print("------------------")
print("Enter subject name: ")
subject = input()
print("Enter maximum score:")
max_score = int(input())
print("Enter your score: ")
score = int(input())
total = float((score/max_score)*100)
Grade = round(total, 2)
if ((score >= 90) and (score <= 100)):
  print("Your percentage in",subject,"=",Grade)
  print("Grade A+")
elif ((score >= 80) and (score <= 89)):
  print("Your percentage in",subject,"=",Grade)
  print("Grade A")
elif ((score >= 70) and (score <= 79)):
  print("Your percentage in",subject,"=",Grade)
  print("Grade B")
elif ((score >= 60) and (score <= 69)):
  print("Your percentage in",subject,"=",Grade)
  print("Grade C")
elif ((score >= 50) and (score <= 59)):
  print("Your percentage in",subject,"=",Grade)
  print("Grade D")  
elif (score <= 50):
  print("Under 50")
else:
  print("Enter Your marks again")
  

