#  List Generator
print("List Generator")
print("----------------")
print()
start = int(input("Start number at: "))
end = int(input("End Before this number: "))
incremenet = int(input("Incremment: "))

for i in range (start, end, incremenet):
  print(i)
