# -*- coding: utf-8 -*-
"""
Exercise 4: Primitive Quiz - 30 Marks
@author: Reyn Blessil Santos
"""
#i get an input from the user, must be a string since the capital of france is concatenation of letters
response = input("What is the capital of France?")
if response == "Paris": #i used an if statement so that if the user input response is 'Paris' then the program will output the answer is correct
    print("Congratulations! Your answer is correct.")
else: #otherwise if the user did not input 'Paris' then the program will output incorrect
    print("Your answer is incorrect.")
    
    
#ADVANCED REQUIREMENTS
response=input("What is the capital of France?") #similar to the basic requirement, i asked for the user input but this time i included emphasized user input must be a string
response = response.lower() #this method turns all of the letters in the user input to lowercase letters
if response == "paris":#so that when the response enters the if statement, then an answer of all lowercase 'paris' would be correct regardless of what the user capitalized originally
    print("Congratulations! Your answer is correct.")
else: #otherwise the program will output incorrect
    print("Your answer is incorrect.")
    
#the rest of the code works the same for different countries and capitals
response = input("What is the capital of Albania?")
response = response.lower()
if response == "tirana":
    print("Congratulations! Your answer is correct.")
else:
    print("Your answer is incorrect.")
    
response = input("What is the capital of Andorra?")
response = response.lower()
if response == "andorra la vella":
    print("Congratulations! Your answer is correct.")
else:
    print("Your answer is incorrect.")
    
response = input("What is the capital of Austria?")
response = response.lower()
if response == "vienna":
    print("Congratulations! Your answer is correct.")
else:
    print("Your answer is incorrect.")
    
response = input("What is the capital of Belarus?")
response = response.lower()
if response == "minsk":
    print("Congratulations! Your answer is correct.")
else:
    print("Your answer is incorrect.")
    
response = input("What is the capital of Belgium?")
response = response.lower()
if response == "brussels":
    print("Congratulations! Your answer is correct.")
else:
    print("Your answer is incorrect.")
    
response = input("What is the capital of Bosnia and Herzegovina?")
response = response.lower()
if response == "sarajevo":
    print("Congratulations! Your answer is correct.")
else:
    print("Your answer is incorrect.")
    
response = input("What is the capital of Bulgaria?")
response = response.lower()
if response == "sofia":
    print("Congratulations! Your answer is correct.")
else:
    print("Your answer is incorrect.")
    
response = input("What is the capital of Crotia?")
response = response.lower()
if response == "zagreb":
    print("Congratulations! Your answer is correct.")
else:
    print("Your answer is incorrect.")
    
response = input("What is the capital of Cyprus?")
response = response.lower()
if response == "nicosia":
    print("Congratulations! Your answer is correct.")
else:
    print("Your answer is incorrect.")
