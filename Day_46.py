dict = {}

def prettyPrint():
   for key,value in dict.items():
      print(key, end=": ")
      for subkey, subvalue in value.items():
         print(subkey,subvalue, end= " | ")
   print()
      
while True:
   print()
   name = input("Enter Beast name: ").title()
   type = input("Enter Type name: ")
   special_move = input("Enter special Move: ")
   strength = input("Enter Strength HP: ")

   dict[name] = {"Special Move" : special_move, "Strength": strength}
   print()

   prettyPrint()
