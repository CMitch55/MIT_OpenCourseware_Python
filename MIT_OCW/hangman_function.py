#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 19:08:41 2020

This program is a test bed for the show_possible_matches function for the hangman game.

Presenting the function with the current guessed word, which would be a word the
correctly guessed letters and _ , e.g. "a _ _ l _" and serch the word list for all
words with letters in the same index as the letters already guessed in the currently
guessed word.

@author: nmeece
"""

WORDLIST_FILENAME = "/home/nmeece/Repo/MIT_OpenCourseware_Python/MIT_OCW/MIT_OCW_PSets/PS2 Hangman/words.txt"
my_word = "ap_l_"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

wordlist = load_words()


match_list = []
new_match_list = []
match_list_position = 0
   
for word in wordlist:
    if len(word) == len(my_word):
        match_list.append(word)   

new_match_list = match_list[:]
    
for match_len_word in match_list:
    # print('Current word being evaluated: ', match_len_word)
        
    match_word_position = 0
        
    for letter in match_len_word:
        # print(match_len_word, "index", match_word_position, "is", letter)
        if my_word[match_word_position] == "_" or my_word[match_word_position] == letter:
            # print("That means that ", my_word[match_word_position], "is == to:", letter, "or _")
            match_word_position += 1
            
        else:
            # print("That means that", my_word[match_word_position], "!=", letter)
            new_match_list.remove(match_len_word)
            break
    
    match_list_position += 1
    
if len(new_match_list) == 0:
    print("No matches found.")
else:
    print(' '.join(new_match_list))
        
