# SOURCE: https://www.educative.io/blog/crack-amazon-coding-interview-questions#questions
# 1. Find the missing number in the array
'''You are given an array of positive numbers from 1 to n,
such that all numbers from 1 to n are present except one number x.
You have to find x. The input array is not sorted. Look at the
below array and give it a try before checking the solution.'''
def find_missing(input):
    n = len(input) + 1
    supposed_sum = (n*(n+1))/2
    missing = int(supposed_sum - sum(input))
    return missing

find_missing([1,2,4,5])