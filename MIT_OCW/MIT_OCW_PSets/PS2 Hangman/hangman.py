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
    
    for char in avail_letters:
        if char in letters_guessed:
            avail_letters.remove(char)
        else:
            pass
    
    return''.join(avail_letters)
    
wordlist = load_words()
letters_guessed = []
max_num_guesses = 6   

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
    current_num_guesses = 0
    max_num_warnings = 3
    current_num_warnings = 0
    vowels = ["a", "e", "i", "o", "u"]
    
    print("Howdy! Welcome to the game Hangman!") 
    print("I am thinking of a word", len(secret_word), "letters long!")
    print("You have", max_num_warnings - current_num_warnings, "warnings left.")
    
    while (max_num_guesses - current_num_guesses) >= 1 and is_word_guessed(secret_word, letters_guessed) is False:
        
        print("-------------")
        print("You have ", max_num_guesses - current_num_guesses, "guesses left.")
        print("Available letters: ", get_available_letters(letters_guessed))
        user_guess = str.lower(input("Please guess a letter:"))
    
        if str.isalpha(user_guess) is False or len(user_guess) > 1:
            if max_num_warnings - current_num_warnings >= 1:
                current_num_warnings += 1
            else:
                current_num_guesses += 1
            print("Oops! That is not a vaild letter! You have", max_num_warnings - current_num_warnings, "warnings left: ", get_guessed_word(secret_word, letters_guessed))
       
        elif user_guess not in secret_word:
            
            if user_guess in vowels and user_guess not in letters_guessed:
                letters_guessed.append(user_guess)
                current_num_guesses += 2
                print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
            elif user_guess in vowels and user_guess in letters_guessed:
                if max_num_warnings - current_num_warnings >= 1:
                    current_num_warnings += 1
                    print("Oops! You've already guessed that letter. You now have", max_num_warnings - current_num_warnings, "warnings left: ", get_guessed_word(secret_word, letters_guessed))
                else:
                    current_num_guesses += 1
                    print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
            else:
                current_num_guesses += 1
                print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
        
        elif user_guess in letters_guessed:
        
            if max_num_warnings - current_num_warnings >= 1:
                current_num_warnings += 1
                print("Oops! You've already guessed that letter. You now have", max_num_warnings - current_num_warnings, "warnings left: ", get_guessed_word(secret_word, letters_guessed))
            else:
                current_num_guesses += 1
            
        
        else:
            letters_guessed.append(user_guess)
            print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
            
        
        if current_num_guesses >= 6:
            print("-----------")
            print("You lose! The secret word was: ", secret_word) 
            
        elif is_word_guessed(secret_word, letters_guessed) is True:
            unique_letters = []
            for char in secret_word:
                if char not in unique_letters:
                    unique_letters.append(char)
                
            print("Congratulations, you win!")
            print("Your total score for this game is: ", (max_num_guesses - current_num_guesses) * int(len(unique_letters)))
                                   
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
    
    my_split_word = my_word.split()    
    letter_list = my_word.split('_')
    letters_guessed = ''.join(letter_list)
    word_position = 0
    
    for char in my_split_word:
        
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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = "apple" #choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
