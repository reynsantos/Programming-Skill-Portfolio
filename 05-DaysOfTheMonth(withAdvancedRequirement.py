# -*- coding: utf-8 -*-
"""
Exercise 5: Days of the Month - 30 Marks
"""
#i created a dictionary, in which its keys are assigned by numbers 1 to 12 for each day of the month, and its values carry the number of days in each of those months
months = {
    '1': 31,
    '2': 28,
    '3': 31,
    '4': 30,
    '5': 31,
    '6': 30,
    '7': 31,
    '8': 31,
    '9': 30,
    '10': 31,
    '11': 30,
    '12': 31
} #dictionaries use curly braces, while lists use square brackets

user=int(input("Input the month number (1-12): ")) #i ask for the user input of which month they would like to know the number of days in it (it should be an integer)

if 1 <= user <= 12: #the program then enters an if statement where the user input should be between 1-12, since negative numbers are unapplicable and there are only 12 months in a year
    print(months[str(user)]) #if the input was between 1-12 then the program will print the number of days in chosen month
else:
    print("Please input a valid integer between 1 and 12.") #otherwise the program will ask for a user input of an integer between 1-12
    
#Advanced Requirement:
months = {
    '1': 31,
    '2': 28,
    '3': 31,
    '4': 30,
    '5': 31,
    '6': 30,
    '7': 31,
    '8': 31,
    '9': 30,
    '10': 31,
    '11': 30,
    '12': 31
} #similar to basic requirements, i created the same dictionary

user = int(input("Input the month number (1-12): ")) #i asked for user input


if 1 <= user <= 12: #program can only enter this loop if the integer that the user input is between 1-12
    if user == 2: #if the user input '2' which is february, it will ask whether it is a leap year or not
        leap = input("Is it a leap year? ") 
        leap.lower() #i included a function that lowercases the user's input for functionality
        if leap == "yes": #if the user input is yes that it is in fact a leap year, then the program will print '29'
            months['2']= 29
            print(months['2'])
        else: #otherwise it will print '28' the original value of the '2' key in my dictionary above
            print(months[str(user)])

        
else: #the program will run this else statement if the user inputs an integer value that is not between 1-12
    print("Please input a valid integer between 1 and 12.")