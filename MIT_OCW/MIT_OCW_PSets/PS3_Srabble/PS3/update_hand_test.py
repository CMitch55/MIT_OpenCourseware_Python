'''
A place outside of my core program to play with the update_hand function.

Nygel M.
29DEC2020
'''

hand = {'i':1, 'v':2, 'l':2, 'e':1, 'n':1, '7':2}
word = 'Evil'
low_word = str.lower(word)
new_hand = hand.copy()

for letter in low_word:
    if letter in new_hand and new_hand[letter] >= 1:
        print(letter)
        new_hand[letter] -= 1
        if new_hand[letter] <= 0:
            del(new_hand[letter])
    else:
        continue

print(new_hand)

