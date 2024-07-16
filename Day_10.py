# Extend your bill calculator --
TotalBill = float(input("Total bill: "))
numberOfPeople = int(input("Number of person: "))
tip = float(input("Percentage of tip: "))
tip = (tip/100)*TotalBill
amount = (TotalBill+tip) / numberOfPeople
amount = round(amount, 2)
print("For eaach person have to paid: ₹", amount)

