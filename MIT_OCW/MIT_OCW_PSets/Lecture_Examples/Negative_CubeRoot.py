# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 15:34:49 2020

@author: Nygel
"""

####################
## EXAMPLE: bisection cube root (only positive cubes!)
####################
cube = 0.5
#cube = 8120601
# won't work with x < 1 because initial upper bound is less than ans
#cube = 0.25
epsilon = 0.01
num_guesses = 0
low = 0
high = cube

if (cube > 0 and cube < 1) or (cube > -1 and cube < 0):
        low = abs(cube)
        high = 1
        
guess = (high + low)/2.0

while abs(guess**3 - cube) >= epsilon:
    print(guess)
            
    if guess**3 < cube:
        # look only in upper half search space
        low = guess
    else:
        # look only in lower half search space
        high = guess
    # next guess is halfway in search space
    guess = (high + low)/2.0
    num_guesses += 1
    
    # if num_guesses == 20:
#        break
print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)
   