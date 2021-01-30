#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 21:28:08 2020

@author: nmeece
"""

warning = 3
guesses



def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    
    guesses = 6
    warnings = 3
    
    vowels = ["a", "e", "i", "o", "u"]
    
    print("Howdy! Welcome to the game Hangman!") 
    print("I am thinking of a word", len(secret_word), "letters long!")
    print("You have", max_num_warnings - current_num_warnings, "warnings left.")
    
    while guesses >=1 and is_word_guessed(secret_word, letters_guessed) is False:
        
        print("-------------")
        print("You have ", guesses, "guesses left.")
        print("Available letters: ", get_available_letters(letters_guessed))
        user_guess = str.lower(input("Please guess a letter:"))
        
        if str.isalpha(user_guess) is False or len(user_guess) > 1:
            if warnings >= 1:
                warnings -= 1
            else:
                guesses -= 1
            print("Oops! That is not a vaild letter! You have", warnings, "warnings left: ", get_guessed_word(secret_word, letters_guessed))
            
            
        if user_guess in letters_guessed:
            if warnings >= 1:
                warnings -= 1
                print("Oops! You've already guessed that letter. You now have", warnings, " warnings remaining.", get_guessed_word(secret_word, letters_guessed)
            else:
                guesses -= 1
                print("Oops! You've already guessed that letter. You now have", guesses, "guesses remaining.", get_guessed_word(secret_word, letters_guessed)

        elif user_guess not in secret_word:
            if user_guess in vowels:
                letters_guessed.append(user_guess)
                guesses -= 2
            else:
                letters_guessed.append(user_guess)
                guesses -= 1
                
        else:
            letters_guessed.append(user_guess)
            print("Good guess:" get_guessed_word(secret_word, letters_guessed))
        
        if guesses <= 0:
            print("-----------")
            print("You lose! The secret word was: ", secret_word) 
            
        if is_word_guessed(secret_word, letters_guessed) is True:
        
            unique_letters = []
            
            for char in secret_word:
                if char not in unique_letters:
                    unique_letters.append(char)
                
            print("Congratulations, you win!")
            print("Your total score for this game is: ", guesses * int(len(unique_letters)))
                
                
                
                
                