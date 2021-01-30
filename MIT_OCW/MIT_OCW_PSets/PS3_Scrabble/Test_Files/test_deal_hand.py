'''
Testbench to unit test the deal_hand function of ps3.py.
The most recent version of deal_hand should deal 1 wildcard
guranteed followed by the rest of the hand. deal_hand should 
return a dictionary with a number of characters = n where at
least one character is a wildcard.

N. Meece
01/01/2021
'''

import ps3 as scrabble

if type(scrabble.deal_hand(7)) == type(dict):
    print('True')

# n = 7 
#x = [7]
#y = {7:0}
#z = (7)

#print('When deal_hand is given', n, 'an object of type', str(type(n)), 'deal_hand returns:', scrabble.deal_hand(n))

#print('When deal_hand is given', x, 'an object of type', str(type(x)), 'deal_hand returns:', scrabble.deal_hand(x))

#print('When deal_hand is given', y, 'an object of type', str(type(y)), 'deal_hand returns:', scrabble.deal_hand(y))

#print('When deal_hand is given', z, 'an object of type', str(type(z)), 'deal_hand returns:', scrabble.deal_hand(z))

def test_wildcard_deal_hand():
    '''
    Unit test for deal_hand
    '''
    # Test 1 - deal_hand given an int
    n = 7
    hand = scrabble.deal_hand(n)
    if hand.get('*') == 1 and len(hand) == n:
        print('SUCCESS: When given', type(n), 'of value:', n, '.')
        print('deal_hand returns:', type(hand), 'of value:', str(hand))

        return # exit function

test_wildcard_deal_hand()