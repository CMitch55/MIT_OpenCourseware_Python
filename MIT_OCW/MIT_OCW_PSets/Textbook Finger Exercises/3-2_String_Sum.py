# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 12:58:52 2020

Finger Exercise for section 3.2 of the Introduction to Comoputation and Programming Using Python textbook.

Prompt:
    Let s be a string that contains a sequence of decimal numbers seperated by commas, e.g., s = '1.23,2.4,3.123'.
    Write a program that prints the sum of the numbesr in s.

@author: Nygel
"""

total   = 0
s       = '1.23,2.4,3.123,25.2,34.762'
SliceCount = 0
start   = 0

for i in s:
    # print(SliceCount)
    if i != "," and SliceCount == (len(s) - 1):        
        total += float(s[start:len(s)])

    elif i != ",":
        SliceCount += 1
        
    else:
        # print(s[start:SliceCount])
        total += float(s[start:SliceCount])
        SliceCount += 1
        start = SliceCount
        # print(SliceCount)

print("Final Total: ", total)