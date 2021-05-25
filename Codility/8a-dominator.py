'''DOMINATOR
https://app.codility.com/programmers/lessons/8-leader/dominator/

An array A consisting of N integers is given. The dominator of array A is the
value that occurs in more than half of the elements of A.

For example, consider array A such that
 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3

The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely
in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

Write a function

    def solution(A)

that, given an array A consisting of N integers, returns index of any element
of array A in which the dominator of A occurs. The function should return −1 if
array A does not have a dominator.

For example, given array A such that
 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3

the function may return 0, 2, 4, 6 or 7, as explained above.

Write an efficient algorithm for the following assumptions:

    N is an integer within the range [0..100,000];
    each element of array A is an integer within the range
        [−2,147,483,648..2,147,483,647].
'''
def solution(A):
    my_dictionary = {}

    for item in A:
        my_dictionary[item] = 0

    for item in A:
        my_dictionary[item] += 1

    have_dominator = False
    value_dominator = -1
    index_dominator = -1

    for index in range( len(A) ):
        if my_dictionary[ A[index] ] > float(len(A) / 2):
            have_dominator = True
            value_dominator = A[index]
            index_dominator = index

    if have_dominator == False:
        return -1
    else:
        return index_dominator


def solution2(A):
    n = len(A)
    size = 0
    for k in range(n):
        if (size == 0):
            size += 1
            value = A[k]
        else:
            if (value != A[k]):
                size -= 1
            else:
                size += 1
    candidate = -1
    if (size > 0):
        candidate = value
    leader = -1
    count = 0
    for k in range(n):
        if (A[k] == candidate):
            count += 1
    if (count > n // 2):
        leader = candidate
    else:
        return -1

    return A.index(leader)