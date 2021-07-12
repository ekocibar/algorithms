"""
https://www.hackerrank.com/challenges/ctci-making-anagrams
"""


import string
def makeAnagram(a, b):
    hash_chars = {char:0 for char in string.ascii_lowercase}

    for char in a:
        hash_chars[char] += 1
    for char in b:
        hash_chars[char] -= 1

    result = sum(map(abs, hash_chars.values()))
    return result