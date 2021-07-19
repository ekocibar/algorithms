'''COUNT DIV
https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/

Write a function:

    def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within
the range [A..B] that are divisible by K, i.e.:

    { i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3,
because there are three numbers divisible by 2 within the range [6..11],
namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

        A and B are integers within the range [0..2,000,000,000];
        K is an integer within the range [1..2,000,000,000];
        A ≤ B.
'''
def solution(A, B, K):
    # need to achieve low complexity O(1)
    # using math equation (low complexity)

    # number of divisible values smaller than B
    num_B = B // K

    # number of divisible values smaller than A
    num_A = A // K

    # number of divisible numbers
    num_divisible = num_B - num_A

    # note: plus one (if A % K == 0)
    # because "A" is also divisble
    plus = 0
    if A % K == 0:
        plus = 1

    num_divisible = num_divisible + plus

    return num_divisible