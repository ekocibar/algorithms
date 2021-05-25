'''COUNT TRIANGLES
https://app.codility.com/programmers/lessons/15-caterpillar_method/count_triangles/

An array A consisting of N integers is given. A triplet (P, Q, R) is triangular
if it is possible to build a triangle with sides of lengths A[P], A[Q] and A[R]
In other words, triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

        A[P] + A[Q] > A[R],
        A[Q] + A[R] > A[P],
        A[R] + A[P] > A[Q].

For example, consider array A such that:
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 12

There are four triangular triplets that can be constructed from elements of
this array, namely (0, 2, 4), (0, 2, 5), (0, 4, 5), and (2, 4, 5).

Write a function:

    def solution(A)

that, given an array A consisting of N integers, returns the number of
triangular triplets in this array.

For example, given array A such that:
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 12

the function should return 4, as explained above.

Write an efficient algorithm for the following assumptions:

    N is an integer within the range [0..1,000];
    each element of array A is an integer within the range [1..1,000,000,000].
'''
def solution(A):
    my_list = A
    my_list.sort()

    if len(A) < 3:
        return 0

    # caterpillar method
    count_triangular = 0
    for index_one in range(len(A) - 2):
        index_two = index_one + 1
        index_three = index_one + 2
        while (index_two < len(A)-1):
            if (index_three < len(A)) and (my_list[index_one] +\
                    my_list[index_two] > my_list[index_three]) :
                index_three += 1
            else:
                count_triangular += (index_three - index_two - 1)
                index_two += 1

    return count_triangular
