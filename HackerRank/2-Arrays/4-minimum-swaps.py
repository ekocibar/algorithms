"""
https://www.hackerrank.com/challenges/minimum-swaps-2
"""

def minimumSwaps(arr):
    swaps = 0
    for i in range(0, len(arr) - 1):
        while arr[i] != i + 1:
            t = arr[arr[i] - 1]
            arr[arr[i] - 1] = arr[i]
            arr[i] = t
            swaps += 1
    return swaps
