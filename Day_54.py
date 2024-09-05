import csv

with open("Day54Totals.csv") as file:
  reader = csv.DictReader(file)
  item = 0
  for row in reader:
      item += float(row["Quantity"]) * float(row["Cost"])
  print(f"Your profit for Today: Rs-> {round(item,2)}")
  
