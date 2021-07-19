''' TAPE EQUILIBRIUM
https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/

A non-empty array A consisting of N integers is given. Array A represents
numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts:
A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of:
|(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part
and the sum of the second part.

For example, consider array A such that:
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3

We can split this tape in four places:

        P = 1, difference = |3 − 10| = 7
        P = 2, difference = |4 − 9| = 5
        P = 3, difference = |6 − 7| = 1
        P = 4, difference = |10 − 3| = 7

Write a function:

    def solution(A)

that, given a non-empty array A of N integers, returns the minimal difference
that can be achieved.

For example, given:
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3

the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [2..100,000];
        each element of array A is an integer within the range [−1,000..1,000].
'''
import sys
# O(n2)
def solution(A):
    INT_MAX = sys.maxsize
    min_diff = INT_MAX

    for index in range(0, len(A)):
        first_total = 0
        for j in range(0, index):
            first_total += A[j]

        second_total = 0
        for k in range(index, len(A)):
            second_total += A[k]

        current_difference = abs( first_total - second_total)
        min_diff = min(min_diff, current_difference)

    return min_diff

# O(n) %84
import sys
def solution2(A):
    right_side = sum(A)
    left_side = 0
    min_diff = sys.maxsize

    for num in A:
        right_side -= num
        left_side += num
        min_diff = min(min_diff, abs(right_side - left_side))
    return min_diff
