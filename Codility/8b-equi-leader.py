'''EQUILEADER
https://app.codility.com/programmers/lessons/8-leader/equi_leader/

A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the
elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences
A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the
same value.

For example, given array A such that:
    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2

we can find two equi leaders:

    0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader,
    whose value is 4.
    2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader,
    whose value is 4.

The goal is to count the number of equi leaders.

Write a function:

    def solution(A)

that, given a non-empty array A consisting of N integers, returns the number of
equi leaders.

For example, given:
    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2

the function should return 2, as explained above.

Write an efficient algorithm for the following assumptions:

    N is an integer within the range [1..100,000];
    each element of array A is an integer within the range
        [−1,000,000,000..1,000,000,000].
'''
def solution(A):
    # write your code in Python 3.6

    # key point:
    # the equi-leader 'must' be leader in A

    # step 1: find the leader in A
    my_dictionary = {}
    for item in A:
        my_dictionary[item] = 0

    for item in A:
        my_dictionary[item] += 1

    have_leader = False
    leader_value = -1
    for item in A:
        if my_dictionary[item] > float(len(A) / 2):
            have_leader = True
            leader_value = item

    if have_leader == False:
        return 0

    # step 2: number of equi-leaders
    leader_count = []
    num_leader = 0
    for item in A:
        if item == leader_value:
            num_leader += 1
            leader_count.append(num_leader)
        else:
            leader_count.append(num_leader)

    num_equi_leader = 0
    for index in range(len(A)):
        total_num_leader = leader_count[len(A)-1]
        left_num_leader = leader_count[index]
        right_num_leader = total_num_leader - left_num_leader
        left_leader_threshold = float( (index+1) / 2)
        right_leader_threshold = float( (len(A)-index-1) / 2)
        if (left_num_leader > left_leader_threshold
                and right_num_leader > right_leader_threshold):
            num_equi_leader += 1

    return num_equi_leader
