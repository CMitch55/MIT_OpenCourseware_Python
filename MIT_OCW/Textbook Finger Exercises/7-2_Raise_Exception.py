'''

Finger Exercise on page 105, section 7.2. Raise an exception.

Nygel Meece
22DEC2020

'''


def findAnEven(L):
    '''Assumes L is a list of integers
    Returns the first even number in L
    Raises ValueError if L does not contain an even number.'''
    loop_count = 0
    for n in L:
        loop_count += 1
        if n % 2 == 0:
            return print(n)
        elif loop_count == len(L):
            raise ValueError

L = [1, 3, 5]

findAnEven([1,5,3])