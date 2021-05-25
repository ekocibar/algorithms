'''MIN MAX DIVISION
https://app.codility.com/programmers/lessons/14-binary_search_algorithm/min_max_division/


You are given integers K, M and a non-empty array A consisting of N integers.
Every element of the array is not greater than M.

You should divide this array into K blocks of consecutive elements. The size of
the block is any integer between 0 and N. Every element of the array should
belong to some block.

The sum of the block from X to Y equals A[X] + A[X + 1] + ... + A[Y]. The sum
of empty block equals 0.

The large sum is the maximal sum of any block.

For example, you are given integers K = 3, M = 5 and array A such that:
  A[0] = 2
  A[1] = 1
  A[2] = 5
  A[3] = 1
  A[4] = 2
  A[5] = 2
  A[6] = 2

The array can be divided, for example, into the following blocks:

        [2, 1, 5, 1, 2, 2, 2], [], [] with a large sum of 15;
        [2], [1, 5, 1, 2], [2, 2] with a large sum of 9;
        [2, 1, 5], [], [1, 2, 2, 2] with a large sum of 8;
        [2, 1], [5, 1], [2, 2, 2] with a large sum of 6.

The goal is to minimize the large sum. In the above example, 6 is the minimal
large sum.

Write a function:

    def solution(K, M, A)

that, given integers K, M and a non-empty array A consisting of N integers,
returns the minimal large sum.

For example, given K = 3, M = 5 and array A such that:
  A[0] = 2
  A[1] = 1
  A[2] = 5
  A[3] = 1
  A[4] = 2
  A[5] = 2
  A[6] = 2

the function should return 6, as explained above.

Write an efficient algorithm for the following assumptions:

        N and K are integers within the range [1..100,000];
        M is an integer within the range [0..10,000];
        each element of array A is an integer within the range [0..M].
'''
import math

def solution(K, M, A):
    # try to find minMaxSum
    # we can try 'minMaxSum' by using binary search (fast)
    # but, we need to know
    # min_possible_sum and max_possible_sum
    # so, we can try mid_possible_sum (using binary search)

    # 1. find min_possible_sum and max_possible_sum
    min_possible_sum = 0
    max_possible_sum = 0
    for item in A:
        min_possible_sum = max(min_possible_sum, item) # largest element
        max_possible_sum += item # at most all elements (sum of all)

    # 3. check if mid_possible_sum is 'ok' or not (define the method)
    def check_if_mid_sum_possible(K, M, A, mid_sum):
        num_block_allowed = K
        current_block_sum = 0
        for item in A:
            current_block_sum += item
            if current_block_sum > mid_sum: # need another block
                num_block_allowed -= 1
                current_block_sum = item # important (the item in next block)
                if num_block_allowed ==0:
                    return False
        # all blocks can be smaller than (or equal to) mid_sum
        return True

    # 2. binary search
    result = max_possible_sum

    while min_possible_sum <= max_possible_sum:
        mid_possible_sum = math.ceil( (min_possible_sum + max_possible_sum) / 2 )

        # try smaller
        is_sum_possible = check_if_mid_sum_possible(K, M, A, mid_possible_sum)
        if is_sum_possible:
            result = mid_possible_sum
            max_possible_sum = mid_possible_sum - 1

        # try bigger
        else:
            min_possible_sum = mid_possible_sum + 1

    return result
