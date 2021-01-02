'''
Safe space to try writing the is_word_valid function.

Modified to accomodate for wildcards. '*' is the wildcard character.
should a word be entered with a wildcard, the wildcard shall be replaced
by a vowel until a word found in the wordlist is created OR no good word
is found.

Nygel M.
29DEC2020
'''


VOWELS = 'aeiou'
word = "h*ney"
hand = {'n': 1, 'h': 1, '*': 1, 'y': 1, 'd': 1, 'w': 1, 'e': 2}
word_list = ["hello", 'apple', 'honey', 'evil', 'rapture', 'honey']

def is_word_valid(word, hand, word_list):
    
    low_word = str.lower(word)
    hand_copy = hand.copy()
    vowels_list = list(VOWELS)
    wild_guess_list = []
    wild_guess_counter = 0


    while '*' in low_word:
        while len(vowels_list) >= 1 and ''.join(wild_guess_list) not in word_list:
            wild_guess_list = []
            for n in low_word:
                if n != str("*"):
                    wild_guess_list.append(n)
                else:
                    wild_guess_list.append(vowels_list[0])
                    del vowels_list[0]
                    wild_guess_counter += 1
        wild_guess = ''.join(wild_guess_list)
        if wild_guess in word_list:
            for letter in low_word:
                if letter in hand_copy and hand_copy[letter] >= 1:
                    hand_copy[letter] -= 1
                    if hand_copy[letter] <= 0:
                        del(hand_copy[letter])
                else:
                    return print('False')
            return print('True')
        else:
            return print('False')


    while low_word in word_list:
        for letter in low_word:
            if letter in hand_copy and hand_copy[letter] >= 1:
                hand_copy[letter] -= 1
                if hand_copy[letter] <= 0:
                    del (hand_copy[letter])
                continue
            else:
                return print('False')
        return print('True')
    return print('False')

is_word_valid(word, hand, word_list)