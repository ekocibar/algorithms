"""
https://www.hackerrank.com/challenges/angry-children
"""
import sys

def maxMin(k, arr):
    n = len(arr)
    arr.sort()
    min_diff = sys.maxsize
    for index in range(n-k+1):
        min_diff = min((arr[index+k-1] - arr[index]), min_diff)
    return min_diff
