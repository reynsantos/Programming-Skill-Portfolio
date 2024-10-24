# -*- coding: utf-8 -*-
"""
Exercise 6: Brute Force Attack - 30 Marks
@author: Reyn Blessil Santos
"""

password=12345 #i defined the password in an integer
pass1=int(input("Enter your password: "))#i asked the user for an integer user input

while pass1!=password: #i used a while loop that as long as the two integers are not equal to each other, then the program will stay inside the loop
    pass1=input("Password incorrect, please try again. Enter your password: ")
    break #the program only exits the loop if the passwords are now equal to each other
print("Correct password, Welcome!") #the program prints that the password is correct directly after exitting the looop

#Optional Requirements

password=12345 #declared password in an integer variable
pass2=int(input("You have 5 attempts in total. Please enter your password: ")) #asked user for input, also stating that the user has 5 attempts in total
i=1 #initialized the 'i' as my counter
maximum=5 #declared a maximum integer variable to subtract from how many attempts the user has left
remaining=maximum-i
while i<5:
    if pass2!=password: #i then used an if statement so that if the password was not the same, the program would print incorrect
        print(f"Incorrect. You have {remaining} remaining attempts.") #the subtraction represents the number of trials the user has left
        i+=1 #i increment to my i value, otherwise there would be an inifinite loop, since i only want it to repeat 5 times
        remaining=maximum-i
        pass2=int(input("Please enter your password: ")) #it then asks for the password again
    else: #the final else statement states that if the user input the correct password even from first try, it shall not repeat the loop
        print("Correct password.")
        break
    
if password!=pass2: #if the password is the same, the code prints that the user successfully logged in
            print("Inccorect, maximum number of attempts is reached. Be warned that the authorities have been alerted.")
else: #if it is not the same values, the program states that max number is reached and the authorities have been alerted
            print("You have successfully logged in!")
