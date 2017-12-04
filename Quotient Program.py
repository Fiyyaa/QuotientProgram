def divideBySubtraction():
    dividend = float(0)
    divisor = float(0)
    quotient = float(0)
    remainder = float(0)
    newDividend = float(0)
    count = float(0)
    dividend = float(input("Please enter a dividend: "))
    divisor = float(input("Now enter a divisor: "))
    newDividend = dividend
    #print(newDividend)
    while (newDividend >= divisor):
        remainder = newDividend - divisor
        newDividend = remainder
        print(newDividend)
        count += 1
        
    quotient = count
    print(str(dividend) + " divided by " + str(divisor) + " = " + str(quotient)
          + " remainder " + str(remainder))
    
divideBySubtraction()
