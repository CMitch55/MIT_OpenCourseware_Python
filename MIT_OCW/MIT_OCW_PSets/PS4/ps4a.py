# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    try:
        if len(sequence) <= 1:
            return [sequence]
    except TypeError:
        return (print('Object of non-string type passed to get_permutations.'))
    except NameError:
        return (print('get_permutation argument undefined'))
    except SyntaxError:
        return (print('ger_permutation argument syntactically incorrect. Please use a string.'))
    else:
        permutations   = []
        first_char     = sequence[0]
        remaining_char = sequence[1:]
        perms_of_subsequence = get_permutations(remaining_char)
        
        for seq in perms_of_subsequence:
        
            for n in range(len(seq) + 1):
                new_seq = seq[0:n] + first_char + seq[n:len(seq) + 1]
                permutations.append(new_seq)

        return permutations


#print(get_permutations('abc'))

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
    print('Test 1')
    print("Input:", "'pog'")
    print('Expected Output:', ['pog', 'opg', 'ogp', 'gpo', 'gop', 'pgo'])
    print('Actual Output:', get_permutations('pog'))

    print()
    print('------------')
    print()

    print('Test 2')
    print('Input:', "'po'")
    print('Expected Output:', ['po', 'op'])
    print('Actual Output:', get_permutations('po'))

    print()
    print('------------')
    print()

    print('Test 3')
    print('Input:', "'p'")
    print('Expected Output:', ['p'])
    print('Actual Output:', get_permutations('p'))
    

