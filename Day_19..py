print("Loan Calcuclator")
print("--------------------")

loan = int(input("Loan Amount: "))
apr = 0.05
for i in range(10):
  loan+=(loan*apr)
  print(f"Year {i+1} is" ,round(loan,2))
