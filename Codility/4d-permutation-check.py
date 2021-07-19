'''PERMUTATION CHECK
https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/

A non-empty array A consisting of N integers is given.
A permutation is a sequence containing each element from 1 to N once, and only
once.
For example, array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2

is a permutation, but array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3

is not a permutation, because value 2 is missing.
The goal is to check whether array A is a permutation.
Write a function:

    def solution(A)

that, given an array A, returns 1 if array A is a permutation and 0 if it is
not.
For example, given array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2

the function should return 1.
Given array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3

the function should return 0.
Write an efficient algorithm for the following assumptions:

    N is an integer within the range [1..100,000];
    each element of array A is an integer within the range [1..1,000,000,000].
'''
def solution(A):
    sorted_array = sorted(A)
    expected_num = 1
    for item in sorted_array:
        if item == expected_num:
            expected_num += 1
        else:
            return 0

    return 1

# O(n) short (75% needsimprovement)
def solution2(A):
    actual_sum = sum(A)
    n = len(A)
    supposed_sum = (n*(n+1)) // 2

    return 1 if actual_sum == supposed_sum else 0
