# -*- coding: utf-8 -*-
"""
Exercise 8: Simple Search - 30 Marks
"""
#i created a list with square brackets around it and commas separating each string
list=["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] # 0=Jake, 1=Zac, 2=Ian, 3=Ron, 4=Sam, 5=Dave
print(list[4])#i wanted to print 'Sam', which is index 4 since the index starts from 0

#Optional Requirements
input=int(input("Input a search term: ")) #i asked the user for input of a variable that is an integer
print(list[input])#any number inputted between 0-5 will give a valid input of the names in the list