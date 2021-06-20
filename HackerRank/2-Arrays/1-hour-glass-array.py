"""
https://www.hackerrank.com/challenges/2d-array
"""

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
import sys

def hourglassSum(arr):
    max_hour_glass_sum = (-sys.maxsize)-1
    for i in range(4):
        for j in range(4):
            hour_glass_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2]\
                                     + arr[i+1][j+1] +\
                             arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]

            max_hour_glass_sum = max(max_hour_glass_sum, hour_glass_sum)

    return max_hour_glass_sum
