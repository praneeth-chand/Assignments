def factorial(n):
  if n ==0 or n==1:
    return 1
  elif n<0:
    return "factorial cant be defined for negative numbers"
  else:
    return n*factorial(n-1)
n = int(input())
print(factorial(n))

