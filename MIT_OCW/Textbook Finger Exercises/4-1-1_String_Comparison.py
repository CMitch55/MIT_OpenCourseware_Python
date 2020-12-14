# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 14:43:07 2020

Finger Exercise 4.1.1 of the Introduction to Computation and Programming Using Python textbook.

Prompt:
    Write a function isIn that accepts two strings as arguments and returns TRUE if either string occurs anywhere in the other,
    and FALSE otherwise.



@author: Nygel
"""

def isIn(x, y):
    if str(x) in str(y) or str(y) in str(x):
        print("True")
    else:
        print("False")

isIn("fun", "on")