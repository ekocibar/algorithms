"""
https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array
"""

def minimumAbsoluteDifference(arr):
    arr.sort()
    min_diff = abs(arr[1] - arr[0])
    for index in range(1, len(arr)):
        min_diff = min(abs(arr[index] - arr[index-1]), min_diff)
    return min_diff
