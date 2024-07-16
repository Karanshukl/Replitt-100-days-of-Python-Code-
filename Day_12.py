# Fixed code here --
print("100 Days of Code QUIZ")
print()
print("How many can you answer correctly?")   #Add " Double prime 
ans1 = ("What language are we writing in?")
if ans1 == "python"or ans1 == "Python":     
  print("Correct")
else:
  print("Nope🙈")        #Add " double prime or ) closing bracket 
  
ans2 = int(input("Which lesson number is this?"))   #Add int() function
if(ans2>12):
  print("We're not quite that far yet")    #Add indentation 
elif(ans2==12):                           #Re-arrrange elif statement 
  print("That's right!")
else:
  print("We've gone well past that!")
