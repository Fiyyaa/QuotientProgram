This program takes any two integers given by the user's input and uses the process of division by subtraction to divide them. The process of division by subtraction works because when we break it down, we can see that the count in my program is the quotient. This is because the count is just the amount of times we iterate through the loop, in other words, it's the amount of times we can "fit" the divisor into the dividend. As for the remainder, this works because as we subtract the divisor from the dividend, we are breaking down the two numbers until the dividend is less than the divisor. This is relavent because once the dividend is less than the divisor, the divisor will no longer go into the dividend, thus, we are left with the remaining amount.

To run: 
run via idle for python
enter a dividend and divisor

Source code:

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
