"""
https://www.hackerrank.com/challenges/special-palindrome-again/
"""

def substrCount(n, s):
    tot = 0
    count_sequence = 0
    prev = ''
    for i,v in enumerate(s):
        # first increase counter for all seperate characters
        count_sequence += 1
        if i and (prev != v):
            # if this is not the first char in the string
            # and it is not same as previous char,
            # we should check for sequence x.x, xx.xx, xxx.xxx etc
            # and we know it cant be longer on the right side than
            # the sequence we already found on the left side.
            j = 1
            while ((i-j) >= 0) and ((i+j) < len(s)) and j <= count_sequence:
                # make sure the chars to the right and left are equal
                # to the char in the previous found squence
                if s[i-j] == prev == s[i+j]:
                    # if so increase total score and step one step further out
                    tot += 1
                    j += 1
                else:
                    # no need to loop any further if this loop did
                    # not find an x.x  pattern
                    break
            #if the current char is different from previous, reset counter to 1
            count_sequence = 1
        tot += count_sequence
        prev = v
    return tot

# ALTERNATIVE SOLUTION
def substrCount2(n, s):

    palindrome_count = 0
    for i in range(n):
        j = 0

        # Loop while incrementing j, and until a palindrome is found
        while i+j < n and s[i] == s[i+j]:
            j += 1
            palindrome_count += 1

        # s[i+j] is either at the end of the string, or a new letter.

        # Continues if if i+j+j is larger than the string
        if i+j+j > n:
            continue

        # Check that each character after i+j, until i+j+j is the same as our start character
        for _ in range(1, j+1):
            if i+j+_ >= n or s[i] != s[i+j+_]:
                break
        else:
            palindrome_count += 1
    return palindrome_count
