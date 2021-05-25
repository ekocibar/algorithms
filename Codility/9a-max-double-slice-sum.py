'''MAX DOUBLE SLICE SUM
https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_double_slice_sum/

A non-empty array A consisting of N integers is given.

A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.

The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... +
    A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

For example, array A such that:
    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2

contains the following example double slices:

        double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
        double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
        double slice (3, 4, 5), sum is 0.

The goal is to find the maximal sum of any double slice.

Write a function:

    def solution(A)

that, given a non-empty array A consisting of N integers, returns the maximal
sum of any double slice.

For example, given:
    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2

the function should return 17, because no double slice of array A has a sum of
greater than 17.

Write an efficient algorithm for the following assumptions:

    N is an integer within the range [3..100,000];
    each element of array A is an integer within the range [−10,000..10,000].
'''
def solution(A):
    #special case:
    if (len(A) <= 3):
        return 0

    # main idea:
    # use "golden slice algorithm" O(n)
    # take maxEnding[i] = max( 0, maxEnding[i-1] + A[i] ) <--- important~!!
    # explanation :
    # At the end of each slice, we decide whether its value
    # is going to be carried to the next element's computation
    # based on whether the value is "negative or positive". <--- "key point"
    # If positive, we carry it (so it contributes to the next slice)
    # Otherwise we start from "0"

    #(X, Y, Z)
    # 1st slice: A[X+1] + ... + A[Y-1]
    # 2nd slice: A[Y+1] + ... + A[Z-1]
    # Key Point:
    # The array will be split at "Y"
    # main idea:
    # if the middle point is "Y",
    # find "maxLeft" and "maxRight"

    maxLeft = [0] * len(A)
    maxRight = [0] * len(A)

    # 1) find "maxLeft"
    # maxLeft[i] is the maximum sum "contiguous subsequence" ending at index i
    # note: because it is "contiguous", we only need the ending index,important

    for index in range( 1, len(A) ):
    # be careful: from i=1 (because of maxLeft[i-1])
        maxLeft[index] = max(0, maxLeft[index-1]+A[index] );
        # golden slice algorithm: max(0, maxLeft[i-1]+A[i] )

    # 2) find "maxRight"
    for index in range( len(A)-2, -1, -1 ):
    # be careful: from i=A.length-2 (because of maxLeft[i+1])
        maxRight[index] = max(0, maxRight[index+1]+A[index] );
        # golden slice algorithm: Math.max(0, maxRight[i+1]+A[i] )

    # 3) find the maximum of "maxLeft + maxRight"
    maxDoubleSlice = A[1] + A[len(A)-2];
    for index in range( 1, len(A)-1 ):
        if (maxLeft[index-1] + maxRight[index+1]) > maxDoubleSlice:
            maxDoubleSlice = maxLeft[index-1] + maxRight[index+1]
            # be careful: "not" maxLeft[i] + maxRight[i]
            # left end at "i-1", and right begins at "i+1"

    return maxDoubleSlice
