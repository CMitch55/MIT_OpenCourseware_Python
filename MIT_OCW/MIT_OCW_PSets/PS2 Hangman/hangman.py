# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
      
    For each letter in the secret_word, evaluate if the letter doesn't appear in
    the list of letters_guessed.
        If it doesn't, return False.
        OTHERWISE, return True.
    '''

    
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
        
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
      
    For every element of the secret_word, check if the element can be found in
    the letters_guessed list.
        If the element occurs in the letters_guessed list, add it to the current_guess list.
        OTHERWISE, add " _ " to the current_guess list.
    
    Return the current_guess list as a string via ''.join, which should now be
    formatted to fill in the correclty guessed letters and leave the remaining
    letters as blanks.
    '''
    
    current_guess = []
    
    for secret_letter in secret_word:
        if secret_letter not in letters_guessed:
            current_guess.append(" _ ")
        else:
            current_guess.append(secret_letter)
    return ''.join(current_guess)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
      
    Clone list of lowercase letters to vairiable avail_letters.
    
    For each element in avail_letters, check if it occurs in letters_guessed.
        If element is found in letters_guessed, remove it from the list of 
        avail_letters.
        Otherwise, pass.
    Return the string of avail_letters.
    '''
    
    
    avail_letters = list(string.ascii_lowercase)[:]
    
    for char in letters_guessed:
        if char in avail_letters:
            avail_letters.remove(char)
        else:
            pass
    
    return''.join(avail_letters)
    

def repeat_warn_message(warnings):
    '''
    warnings: count of remaining warnings
    
    Returns a print statement informing the user of a repeated answer and
    reports the remaining number of warnings as well as the currently guessed 
    letters so far.
    '''
    return print("Oops! You've already guessed that letter. You now have",
                 warnings, " warnings remaining.", "\nPlease guess a letter:",
                 get_guessed_word(secret_word, letters_guessed))


def repeat_guess_message(guesses):
    '''
    guesses: count of remaining guesses
    
    Returns a print statement informing the user of a repeated answer and 
    reports the remaining number of guesses as well as the currently guesssed
    letters so far.
    '''
    return print("Oops! You've already guessed that letter. You have no",
                 guesses, "guesses remaining.", "\nPlease guess a letter:",
                 get_guessed_word(secret_word, letters_guessed))


def invalid_warn_message(warnings):
    '''    
    warnings: count of remaining warnings
    
    Returns: print statement giving current warning count and guessed word
    '''
    return print("Oops! That isn't a vaild input. You have", warnings,
                 "warnings left.","\nPlease guess a letter:",
                 get_guessed_word(secret_word, letters_guessed))


def invalid_guess_message(guesses):
    '''    
    guesses: count of remaining guesses
    
    returns: print statement giving current guess count and guessed word
    '''
    if guesses >= 1:
        return print("Oops! That isn't a vaild input. You now have", guesses,
                 "guesses remaining.","\n Please guess a letter:",
                 get_guessed_word(secret_word, letters_guessed))
    else:
        return print("Oops! That isn't a valid input:", 
                     get_guessed_word(secret_word, letters_guessed))


def wrong_message():
    '''    
    returns: print statement informing user their guess wasn't in the secret
    word and prints the currently guessed word.
    '''
    return print("Oops! That letter is not in my word.", "\nPlease guess a letter:",
                 get_guessed_word(secret_word, letters_guessed))


def lose_message(secret_word):
    return print("-----------", "\nYou lose! The secret word was: ", secret_word)


wordlist = load_words()
letters_guessed = []

def win_message(guesses, unique_letters):
    return print("------------- \nCongratulations, you win!", 
                 "\nYour total score for this game is:",
                  guesses * int(len(unique_letters)))

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
    print("I am thinking of a word that is", len(secret_word), "letters long!")
    print("You have", warnings, "warnings left.")
    
    while guesses >=1 and is_word_guessed(secret_word, letters_guessed) is False:
        
        print("-------------")
        print("You have", guesses, "guesses left.")
        print("Available letters: ", get_available_letters(letters_guessed))
        user_guess = str.lower(input("Please guess a letter:"))
        
        while str.isalpha(user_guess) is True and len(user_guess) == 1:
                       
            if user_guess in letters_guessed:
                if warnings >= 1:
                    warnings -= 1
                    repeat_warn_message(warnings)
                    break
                else:
                    guesses -= 1
                    repeat_guess_message(guesses)
                    break
                
            elif user_guess not in secret_word:
                if user_guess in vowels:
                    letters_guessed.append(user_guess)
                    guesses -= 2
                else:
                    letters_guessed.append(user_guess)
                    guesses -= 1
                wrong_message()
                break
                    
            else:
                letters_guessed.append(user_guess)
                print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
                break
            
            
        while str.isalpha(user_guess) is False or len(user_guess) != 1:
            if warnings >= 1:
                warnings -= 1
                invalid_warn_message(warnings)
                break
            else:
                guesses -= 1
                invalid_guess_message(guesses)
                break
            
        if is_word_guessed(secret_word, letters_guessed) is True:    

            unique_letters = []

            for char in secret_word:
                if char not in unique_letters:
                    unique_letters.append(char)
            
            win_message(guesses, unique_letters)
    
    if guesses <= 0:
        lose_message(secret_word)
                                
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    
        
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

    
def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word  are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    match_list = []
    match_len_list = []
    guess_list = []
    my_word_list = my_word.split()
    my_joined_word = ''.join(my_word_list)
    
    # Start by making a list of only words of the same length as my_word
    for word in wordlist:
        if len(word) == len(my_joined_word):
            match_len_list.append(word)   
    
        
    # Clone the matchlist as to not modify the original
    match_list = match_len_list[:]
    
    
    for match_word in match_list:
        
        if  match_with_gaps(my_joined_word, match_word) is True:
            guess_list.append(match_word)

    
    if len(guess_list) == 0:
        print("No matches found.")
    else:
        print(' '.join(guess_list))
        

def in_letters_guessed(user_guess, letters_guessed):
    if user_guess not in letters_guessed:
        return False
    else:
        return True
    
    pass

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''

    guesses = 6
    warnings = 3
    
    vowels = ["a", "e", "i", "o", "u"]
    
    print("Howdy! Welcome to the game Hangman!") 
    print("I am thinking of a word that is", len(secret_word), "letters long!")
    print("You have", warnings, "warnings left.")
    
    while guesses >=1 and is_word_guessed(secret_word, letters_guessed) is False:
        
        print("-------------")
        print("You have", guesses, "guesses left.")
        print("Available letters: ", get_available_letters(letters_guessed))
        user_guess = str.lower(input("Please guess a letter:"))
        
        if user_guess == "*" and len(user_guess) == 1:
            
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        
        while str.isalpha(user_guess) is True and len(user_guess) == 1:
                       
            if user_guess in letters_guessed:
                if warnings >= 1:
                    warnings -= 1
                    repeat_warn_message(warnings)
                    break
                else:
                    guesses -= 1
                    repeat_guess_message(guesses)
                    break
                
            elif user_guess not in secret_word:
                if user_guess in vowels:
                    letters_guessed.append(user_guess)
                    guesses -= 2
                else:
                    letters_guessed.append(user_guess)
                    guesses -= 1
                wrong_message()
                break
                    
            else:
                letters_guessed.append(user_guess)
                print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
                break
            
            
        while str.isalpha(user_guess) is False or len(user_guess) != 1:
            if user_guess == "*":
                break
            if warnings >= 1:
                warnings -= 1
                invalid_warn_message(warnings)
                break
            else:
                guesses -= 1
                invalid_guess_message(guesses)
                break
            
        if is_word_guessed(secret_word, letters_guessed) is True:    

            unique_letters = []

            for char in secret_word:
                if char not in unique_letters:
                    unique_letters.append(char)
            
            win_message(guesses, unique_letters)
    
    if guesses <= 0:
        lose_message(secret_word)
    



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = "apple" #choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
