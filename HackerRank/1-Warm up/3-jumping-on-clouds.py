"""
https://www.hackerrank.com/challenges/jumping-on-the-clouds
"""

def jumpingOnClouds(c):
    total_jump = 0
    i = 0
    while i < (len(c) - 1):
        if i+2 < len(c) and c[i+2] == 0:
            i += 2
        else:
            i += 1
        total_jump += 1

    return total_jump