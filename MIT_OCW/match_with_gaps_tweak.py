#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 01:28:19 2020

@author: nmeece
"""

word_position = 0
my_split_word = "a__le" #my_word.split()
other_word = 'apple'
    
for char in my_split_word:
    if char == "_" or char == other_word[word_position]:
        word_position += 1
    else:
        print("False")
print('True')