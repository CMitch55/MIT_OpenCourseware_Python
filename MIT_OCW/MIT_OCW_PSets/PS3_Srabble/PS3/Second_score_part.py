'''
Testbed for trying out potential solutions for the second part of the get_word_score function.
The equation is [7 * word_length - 3 * (n - word_length)]

word_length = an arbitrary string
n = represents hand size, arbitrary int >= 0

Nygel M.
23DEC2020
'''


word = "a"
word_length = len(word)
n = 6

def length_hand_score(word, n):
    try:
        second = (7*len(word)-3*(n-len(word)))

        if second <= 0:
            return(int(1))
        else:
            return(int(second))
    except:
        print("Error in calculating word score.")

print(length_hand_score(word, n))