def pallindrome(str):
  if len(str) <= 1:
    print("Palindrome")
  else:
    if str[0] == str[-1]:
      pallindrome(str[1:-1])
    else:
      print("Not a palindrome")
  
str = "racecar"
pallindrome(str)
