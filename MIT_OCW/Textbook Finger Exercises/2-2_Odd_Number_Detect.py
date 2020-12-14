# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 10:31:38 2020

Following the exercise at the end of section 2.2 of Introduction to Comoputation and Programming Using Python textbook,
this program will evaluate the largest odd number out of three given values and return the largest odd value.
If no odd values are detected, the program will return that there aren't any odd numbers.

@author: Nygel
"""

x = int(input("Enter a number for comparison: "))
y = int(input("Enter a number for comparison: "))
z = int(input("Enter a number for comparison: "))


if x % 2 != 0 and x > y and x > z:
    print("The largest odd number is:", x)
elif y % 2 != 0 and y > x and y > z:
    print("The largest odd number is:", y)
elif z % 2 != 0 and z > x and z > y:
    print("The largest odd number is:", z)
else:
    print("There are no odd numbers.")