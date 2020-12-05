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
my_word = "abbbbb_"
other_word = "apple"

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
match_len_list = []
guess_list = []
    
# Start by making a list of only words of the same length as my_word
for word in wordlist:
    if len(word) == len(my_word):
            match_len_list.append(word)   
    
        
    # Clone the matchlist as to not modify the original
    match_list = match_len_list[:]
    
    
for match_word in match_list:
        
   if  match_with_gaps(my_word, match_word) is True:
       guess_list.append(match_word)

    
if len(guess_list) == 0:
    print("No matches found.")
else:
    print(' '.join(guess_list))
        
 
