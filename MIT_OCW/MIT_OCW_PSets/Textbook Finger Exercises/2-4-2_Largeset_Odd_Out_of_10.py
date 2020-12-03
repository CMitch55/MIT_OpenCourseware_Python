# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 11:44:55 2020

Second Finger Exercise of section 2.4 of the Introduction to Computation and Programming Using Python textbook.

Prompt:
    
    Write a program that asks the user to input 10 integers, and then prints the largest odd number that was entered.
    If no odd number was entered, it should print a message to that effect.
    

@author: Nygel
"""

numInts     = 0
List        = []
Big         = 0
evenCount   = 0

while numInts != 10:
    numIn = int(input("Enter value number: "))
    List.append(numIn)
    
    numInts += 1

for n in List:
    if n % 2 != 0 and n > Big:
        Big = n
        
    elif n % 2 == 0:
        evenCount += 1
        
    else:
        break
    
if evenCount == 10:
    print("All Even")

else:
    print("The largest odd number is:", Big)