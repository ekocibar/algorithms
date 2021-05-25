''' MAX COUNTERS
https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/

You are given N counters, initially set to 0, and you have two possible
operations on them:

        increase(X) − counter X is increased by 1,
        max counter − all counters are set to the maximum value of any counter.

A non-empty array A of M integers is given. This array represents consecutive
operations:

        if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
        if A[K] = N + 1 then operation K is max counter.

For example, given integer N = 5 and array A such that:
    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4

the values of the counters after each consecutive operation will be:
    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)

The goal is to calculate the value of every counter after all operations.

Write a function:

    def solution(N, A)

that, given an integer N and a non-empty array A consisting of M integers,
returns a sequence of integers representing the values of the counters.

Result array should be returned as an array of integers.

For example, given:
    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4

the function should return [3, 2, 2, 4, 2], as explained above.

Write an efficient algorithm for the following assumptions:

        N and M are integers within the range [1..100,000];
        each element of array A is an integer within the range [1..N + 1].
'''

def solution(N, A):
    num_counters = N
    my_list = [0] * N

    max_value = 0
    min_value = 0
    for operation in A:
        if operation < N+1:
            # Set min value
            if my_list[operation-1] < min_value:
                my_list[operation-1] = min_value
            # Set max value
            if my_list[operation-1] == max_value:
                max_value += 1

            my_list[operation-1] += 1

        # Set new min value to current max
        elif operation == N+1:
            min_value = max_value

    for i in range(num_counters):
        if my_list[i] < min_value:
            my_list[i] = min_value

    return my_list
