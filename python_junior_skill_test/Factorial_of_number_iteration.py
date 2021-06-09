def factorial(n):
  if n <0:
    return “factorials are not defined for negative numbers”
  else:
    res = 1 
    for i in range(1,n+1):
      res  *=i 
    return res
n = int(input())
print(factorial(n))

