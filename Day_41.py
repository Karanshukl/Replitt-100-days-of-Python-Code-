def mydictionary():
  mydict = {"Name": "Carlos", "Url": "www.carlosking.com", "Description": "Best website for learning 'Python'", "Rating": "*****"}
  for i,j in mydict.items():
    print(f"{i} --> {j}")

  print()
  print(f"Name:\033[33m {mydict['Name']},\033[0m URL: \033[36m{mydict['Url']},\033[0m Description: \033[35m{mydict['Description']},
  \033[0m Rating: \033[31m{mydict['Rating']}\033[0m ")

mydictionary()



# 2 Method

def mydictionary():
  my_web = {"Name": None, "Url": None, "Description": None, "Rating": None}
  for i in my_web.keys():
    my_web[i] = input(f"{i}: ")
    print()

  for i, j in my_web.items():
      print(f"{i}:  {j}")
    
mydictionary()
