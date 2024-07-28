print("..... 30 Days Down .....")
def daysdown():
  for i in range(1, 31):
   thought = input(f"Day {i}:\n")
   print()
   print(f"                       You think Day {i} was")
   print(f"                       {thought}")
   print()

   # OR 
   # text = f"You think Day {i} was"
   # print(f"{text:^number of spaces you want, like 40}")

print(daysdown())
