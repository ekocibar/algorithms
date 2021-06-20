"""
https://www.hackerrank.com/challenges/ctci-array-left-rotation
"""

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#

def rotLeft(a, d):
    actual_rotation = d%len(a)
    return a[actual_rotation:] + a[:actual_rotation]

rotLeft([1,2,3,4,5], 4)