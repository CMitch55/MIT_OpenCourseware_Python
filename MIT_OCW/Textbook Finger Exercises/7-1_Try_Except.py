'''

Finger Excercise on page 102 in section 7.1 to use Try-Except.

Nygel Meece
21DEC2020

'''

def sumDigits(s):
    cur_sum = 0
        
    for n in s:
        try:
            cur_sum += int(n)
           
        except:
            continue
    print(cur_sum)


sumDigits("a2b3c4d5e")
