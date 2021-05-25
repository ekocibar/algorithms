'''MISSING INTEGER
https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/

This is a demo task.

Write a function:

    def solution(A)

that, given an array A of N integers, returns the smallest positive integer
(greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
'''
def solution(A):
    my_dictionary = {}
    for item in A:
        if item not in my_dictionary:
            my_dictionary[item] = 1

    for i in range(1, len(A)+1 ):
        if i not in my_dictionary:
            return i

    return len(A)+1
