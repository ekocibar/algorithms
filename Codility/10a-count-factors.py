'''COUNT FACTORS
https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/count_factors/

A positive integer D is a factor of a positive integer N if there exists an
integer M such that N = D * M.

For example, 6 is a factor of 24, because M = 4 satisfies the above condition
(24 = 6 * 4).

Write a function:

    def solution(N)

that, given a positive integer N, returns the number of its factors.

For example, given N = 24, the function should return 8, because 24 has 8
factors, namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..2,147,483,647].
'''
import math

def solution(N):
    my_dictionary = {}
    # O(n)
    '''
    for n in range( 1, N+1 ):
        if N % n == 0:
            my_dictionary[n] = True
    '''

    # O( log(n) )
    # be careful: we need to check 'math.sqrt(N)+1'
    for n in range(1, int(math.sqrt(N)) + 1):
        if N % n == 0:
            my_dictionary[n] = True
            another_factor = int( N/n )
            my_dictionary[another_factor] = True

    num_factors = len( my_dictionary )

    return num_factors
