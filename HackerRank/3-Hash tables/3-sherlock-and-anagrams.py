"""
https://www.hackerrank.com/challenges/sherlock-and-anagrams
"""

def sherlockAndAnagrams(s):
    n = len(s)
    res = 0
    for i in range(1, n):
        d = {}
        for j in range(n-i+1):
            subs = ''.join(sorted(s[j:j+i]))
            if subs not in d:
                d[subs] = 1
            else:
                d[subs] += 1

            res += d[subs] - 1
    return res