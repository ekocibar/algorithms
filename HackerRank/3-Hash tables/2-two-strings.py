"""
https://www.hackerrank.com/challenges/two-strings
"""

def twoStrings(s1, s2):
    dict = {}
    for char in s1:
        dict[char] = 1

    for char2 in s2:
        if dict.get(char2,0) == 1:
            return 'YES'
    return 'NO'
