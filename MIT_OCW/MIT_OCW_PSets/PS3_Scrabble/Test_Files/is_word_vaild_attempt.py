'''
Safe space to try writing the is_word_valid function.

Nygel M.
29DEC2020
'''

word = "Rapture"
hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u': 1}
word_list = ["hello", 'apple', 'honey', 'evil', 'rapture']

def is_word_valid(word, hand, word_list):
    
    low_word = str.lower(word)
    hand_copy = hand.copy()

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