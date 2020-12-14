# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 11:28:46 2020

First Finger Exercise in section 2.4 of the Introduction to Computation and Programming Using Python textbook.
Replace the cooment in the example code with a while loop.

Prompt the user for how many times to print "X" and then do it.

@author: Nygel
"""

numXs = int(input('How many times should I print the letter X? '))
toPrint = ""

#concatenate X to toPrint numXs times
while (len(toPrint) != numXs):
    toPrint = toPrint + "X"

print(toPrint)