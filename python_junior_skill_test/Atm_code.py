dividend = int(input())
notes = [500,100,50,10,5]
if dividend%5 ==0:
  for divisor in notes:
    quotient = dividend//divisor
    dividend =dividend%divisor
    print(“{0} * {1} = {2}”.format(divisor , quotient , divisor*quotient)
    quotient =0
else:
   print("invalid amount")
