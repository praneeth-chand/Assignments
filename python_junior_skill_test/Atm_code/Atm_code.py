
def Atm_code(dividend):
    notes = [500,100,50,10,5]
    result =[]
    if dividend%5 ==0 and dividend>0 and str(dividend).isalpha() == False:
      for divisor in notes:
        quotient = dividend//divisor
        dividend =dividend%divisor
        result.append('{0}*{1} = {2}'.format(divisor , quotient , divisor*quotient))
        quotient =0
    else:
       return "invalid amount"
    return result
    