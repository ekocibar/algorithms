"""
https://www.hackerrank.com/challenges/crush
"""

def arrayManipulation(n, queries):
    arr = [0]*n
    for a, b, k in queries:
        for i in range(a-1, b):
            arr[i] += k
    return max(arr)
