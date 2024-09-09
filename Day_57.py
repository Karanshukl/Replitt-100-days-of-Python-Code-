def fact(n):
  if n == 0 or n == 1:
    return n
  else:
    return n*fact(n-1)

n = int(input("Enter Number: "))
ans = fact(n)
print(f"Factorial of number {n} is {ans}")
