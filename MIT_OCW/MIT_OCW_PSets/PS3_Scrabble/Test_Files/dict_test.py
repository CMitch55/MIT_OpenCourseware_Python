'''

Testbed to practice manipulating and working with dictionaries in Python.

Nygel M.
23DEC2020

'''


SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

let_dict = SCRABBLE_LETTER_VALUES
word = "Z0qj0Xv0"
lower_word = str.lower(word)


def letter_score(lower_word):
    score = 0
    for letter in lower_word:
        try:
            score += let_dict[letter]
        except KeyError:
            print("Oops!", letter, "is not a letter!")
        except:
            print("Something has gone horribly wrong.")

    return(int(score))

print(letter_score(lower_word))