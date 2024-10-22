# -*- coding: utf-8 -*-
"""
@author: Reyn Blessil Santos
Exercise 3: Biography - 25 Marks
"""
#i created a dictionary with the keys name, hometown, and age. their values store my name, hometown, age.
my_dict={'Name': 'Reyn Santos',
         'Hometown': 'Dubai',
         'Age': 17}


print('\n'.join(f"{key}: {value}" for key, value in my_dict.items()))
#i used a for loop and the format print to print the dictionary on separate lines
#the purpose of the for loop is that it generates a new line for ever value and key in the dictionary, essentially the loop repeats 3 times, one for each line inside my dictionary

#Advanced Requirements
#i got the input from the user
name = input("Enter your full name: ")
hometown = input("Enter your hometown: ")


while True: #i created a while loopp where the program enters a loop if they place type a string data type of letters instead of numbers which is an integer
    try:
        age = int(input("Enter your age: "))  #user input of age
        break  #the loop will exit if input is valid (it is an integer)
    except ValueError: #an invalid input such as 'twenty' will cause the program to remain in the loop until the user inputs a valid integer. not a string
        print("Please enter a valid number for age.")

#after gathering all user input, the program will store all inputs into the changable dictionary
my_dict = {
    'Name': name,
    'Hometown': hometown,
    'Age': age
}

#similar to basic requirements, i used a for loop again to print the dictionary on separate lines with a singular print function
print('\n'.join(f"{key}: {value}" for key, value in my_dict.items()))

