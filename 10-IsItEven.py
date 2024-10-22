# -*- coding: utf-8 -*-
"""
Exercise 10: Is it even? - 35 Marks

@author: Reyn Blessil Santos
"""
#i created a function called 'oddoreven' with the parameter val for the the value that the user inputs in the main function
def oddoreven(val):
    if val%2==0: #i used modulus to determine if the value divided by 2 has no remainder, then it is even
        print("The number you entered is even.")
    else:
        print("The number you entered is odd.") #otherwise val%2==1 is an odd number, because the value divided by two has a remainder
        
val=int(input("Enter a number: ")) #the main function asks for a user input of a value
oddoreven(val) #i then call on the function i made earlier, to determine if the integer that the user input in 'val' is odd or even