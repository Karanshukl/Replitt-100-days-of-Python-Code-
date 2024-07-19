#Create a "Name the Lyrics" game -- 
print("Fill in the blank lyrics! ")
print("(Type in the blank lyrics and see if you are as cool as me.)")
print("---------------------------------------------------------------")
Counter = 1
while True:
  print("Never going to ______ you up.")
  print()
  lyric = input("Type missing word: ")
  if lyric == "give":
    print("You are right!")
    break
  elif lyric == "let":
    print("You are Wrong")
    Counter +=1
  elif lyric == "put":
    print("Try again")
    Counter +=1
  else:
    print("Nope, try again")
    Counter +=1
    
print()    
print("You took", Counter, "Attempts")
print("Thanks for Playing 👌")

