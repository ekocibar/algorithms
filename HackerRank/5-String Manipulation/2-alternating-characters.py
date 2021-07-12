"""
https://www.hackerrank.com/challenges/alternating-characters
"""


def alternatingCharacters(s):
    count = 0
    for index, char in enumerate(s[:len(s)-1]):
        if char == s[index+1]:
            count += 1
    return count
