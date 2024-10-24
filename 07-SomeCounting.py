# -*- coding: utf-8 -*-
"""
@author: Reyn Blessil Santos
Exercise 7: Some Counting - 20 Marks
"""
print("Counts up from 0 to 50 in increments of 1:") #i used a for loop, i is already initialized as 0 if not stated, and repeats 50 times
for i in range(51):
    print(i)
    
print("Counts down from 50 to 0 in decrements of 1:")#i initialized i as 50 and it decrements 1 for 50 times till it reaches 0
for i in range(50,-1,-1):
    print(i)
    
print("Counts up from 30 to 50 in increments of 1:") #i initalized i as 30 and it repeats 20 times to count till 50
for i in range(30,51):
    print(i)
    
print("Counts down from 50 to 10 in decrements of 2:")#i initalized i as 50 and it subtracts 2, 40 times till it reaches its final value is 10
for i in range(50,9,-2):
    print(i)
    
print("Counts up from 100 to 200 in increments of 5:") #i initalized i as 100 and it adds 5, 100 times until the value 200 is reached
for i in range(100,201,5):
    print(i)
