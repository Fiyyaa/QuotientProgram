def divideBySubtraction():
    dividend = float(0) #define all variables.. Had error before with declaring
#all floats on one line, so I did them one by one
    divisor = float(0)
    quotient = float(0)
    remainder = float(0)
    newDividend = float(0)
    count = float(0)
    dividend = float(input("Please enter a dividend: ")) #Takes users input
    divisor = float(input("Now enter a divisor: "))
    newDividend = dividend #Declares newDividend so it can be in the scope
#of the loop
    #print(newDividend) <-- old debugging
    while (newDividend >= divisor): #will stop once newDividend is less than
#divisor
        remainder = newDividend - divisor
        newDividend = remainder
        #print(newDividend) <-- old debugging
        count += 1
        
    quotient = count
    print(str(dividend) + " divided by " + str(divisor) + " = " + str(quotient)
          + " remainder " + str(remainder)) #concantates and prints
    
divideBySubtraction() #calls function
