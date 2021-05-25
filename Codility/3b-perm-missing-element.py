''' PERM MISSING ELEMENT
https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/

An array A consisting of N different integers is given. The array contains
integers in the range [1..(N + 1)], which means that exactly one element is
missing.

Your goal is to find that missing element.

Write a function:

    def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:
  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5

the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..100,000];
        the elements of A are all distinct;
        each element of array A is an integer within the range [1..(N + 1)].
'''
def solution(A):
    N = len(A)
    my_list = [0] * (N+2)

    missing_element = -1
    for index in range(0, N):
        my_list[ A[index] ] += 1

    for index in range(1, N+2):
        if my_list[ index ] == 0:
            missing_element = index

    return missing_element
