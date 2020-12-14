#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 01:28:19 2020

Testbed for the match_with_gaps function for the hangman game. 

@author: nmeece
"""


my_split_word = "ap_le" #my_word.split()
other_word = 'apple'



def match_with_gaps(my_word, other_word):
    
    
    letter_list = my_word.split('_')
    letters_guessed = ''.join(letter_list)
    word_position = 0
    
    for char in my_word:
        
        # Evaluates if the character in my_word is either a "_" and that other_word[same index as the _]
        # isn't a letter that has already been guessed, OR if the character is the same in both.
        
        if char == "_" and other_word[word_position] not in letters_guessed or char == other_word[word_position]:
            word_position += 1
        else:
            return False
    return True

