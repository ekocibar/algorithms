"""
https://www.hackerrank.com/challenges/sherlock-and-valid-string
"""


from collections import defaultdict
def isValid(s):
    letter_counts = defaultdict(int)
    for char in s:
        letter_counts[char] += 1

    counts = letter_counts.values()
    sorted_counts = sorted(counts)

    if len(list(set(sorted_counts)) ) == 1:
        return 'YES'
    elif (len(list(set(sorted_counts)) ) == 2 and sorted_counts[-1] - sorted_counts[-2] == 1):
        return 'YES'
    else:
        return 'NO'


# ALTERNATIVE SOLUTION
def isValid2(s):
    letter_counts = defaultdict(int)
    for char in s:
        letter_counts[char] += 1

    counts = letter_counts.values()
    k = sorted(counts)
    if len(k) == 1:
        return "YES"
    elif k[0] == 1 and k[1] == k[-1]:
        return "YES"
    else:
        return "YES" if k[-1]-k[0] <= 1 and (k[-1] != k[-2] or k[0] == k[-1]) else "NO"