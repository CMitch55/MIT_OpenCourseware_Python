# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        copy_message = self.message_text
        return copy_message

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        copy_list = self.valid_words.copy()

        return copy_list

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        ###BEGIN PSEUDOCODE###

        #import string to utilize ascii_lowercase/uppercase

        #Iterate over lowercase alphabet

            #If ((current index value in alphabet) - (shift)) < 0, add 26. Else, keep current value.

            #Add current character to dictionary as a key with the value determined above.
        
        #Iterate over uppercase alphabet

            #If ((current index value in alphabet) - (shift)) < 0, add 26. Else, keep current value.

            #Add current character to dictionary as a key with the value determined above.
        
        #Return dictionary

        ###END PSEUDOCODE###

        import string

        lower_alpha = string.ascii_lowercase
        upper_alpha = string.ascii_uppercase
        shift_dict = {}

        for letter in lower_alpha:
            index_shift = ((lower_alpha.index(letter)) - shift)
            if index_shift < 0:
                index_shift += 26
            shift_dict[letter] = lower_alpha[index_shift]

        for letter in upper_alpha:
            index_shift = ((upper_alpha.index(letter)) - shift)
            if index_shift < 0:
                index_shift += 26
            shift_dict[letter] = upper_alpha[index_shift]
        
        return shift_dict

        
    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        ###BEGIN PSEUDOCODE###

        #Create the dictionary to be used as the cipher.

        #Get the message text with which to apply the cipher to.

        #Iterate over message text.

            #If the character in the message is non-alpha, add it to the shifted message list as-is.

            #Add the value associated with key[character] to shifted message list.
        
        #Return the shifted message list as a string.

        ###END PSUEDOCODE###

        cipher_dict = self.build_shift_dict(shift)
        message_text = self.get_message_text()
        shifted_message = []

        for char in message_text:
            if char in cipher_dict.keys():
                shifted_message.append(cipher_dict[char])
            else:
                shifted_message.append(char)
        return(''.join(shifted_message))
                

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self, text)
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the classt
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        encryption_dict = self.encryption_dict
        return encryption_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        #Assigns the change_shift "swift" argument to self.shift
        self.shift = shift
        #Generates a new shift dict using the new shift value and assigns it to encryption_dict
        self.encryption_dict = self.build_shift_dict(shift)
        #Generates a new encrypted message using the new shift on the original input string
        self.message_text_encrypted = self.apply_shift(shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        ###BEGIN PSEUDOCODE###

        #Apply a shift value from range 0 - 26 to the encrypted message

            #Split the shifted message

            #Evaluate if/how many words are valid. Add to dictionary as 
            #{shift value : number of good words}

        #Pull the first key with the largest value

        #Return tuple of ((best shift value), (apply_shift(enc_message, best shift value)))

        ###END PSEUDOCODE###

        word_list = self.get_valid_words()
        good_word_test = []
        decrypt_results = []

        #Using every possible shift value one at a time to decrypt input message, then split
        #individual words seperated by a space into a list.
        for char in range(26):
            decrypted_message = self.apply_shift(char)
            decrypted_words = decrypted_message.split(' ')
            good_word_test = []

            #Evaluate each word in the decrypted message list to determine if they are valid
            #words or not. Done by appending 1 to a list for each good word.
            for word in decrypted_words:
                if is_word(word_list, word):
                    good_word_test.append(1)
                else:
                    good_word_test.append(0)

            #Keep a running list of results for each shift value represented as a tuple of:
            #((total number of good words for a shift value), (shift value), (decrypted message))
            decrypt_results.append((sum(good_word_test), char, decrypted_message))

        #Find a a solution with or tied for the greatest number of valid words. Strip off the
        #number of good words and return the shift value used and the decrypted message.
        best_decrypt = max(decrypt_results)
        solution = best_decrypt[1:3]
        return solution       

if __name__ == '__main__':

#    #Example test case (PlaintextMessage)
#    plaintext = PlaintextMessage('hello', 2)
#    print('Expected Output: jgnnq')
#    print('Actual Output:', plaintext.get_message_text_encrypted())
#
#    #Example test case (CiphertextMessage)
#    ciphertext = CiphertextMessage('jgnnq')
#    print('Expected Output:', (24, 'hello'))
#    print('Actual Output:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE

    #TODO: best shift value and unencrypted story 
    
    pass #delete this line and replace with your code here
