''' MAXIMUM BINARY GAP
https://app.codility.com/programmers/lessons/1-iterations/binary_gap/

A binary gap within a positive integer N is any maximal sequence of consecutive
zeros that is surrounded by ones at both ends in the binary representation of N

For example, number 9 has binary representation 1001 and contains a binary gap
of length 2. The number 529 has binary representation 1000010001 and contains
two binary gaps: one of length 4 and one of length 3. The number 20 has binary
representation 10100 and contains one binary gap of length 1. The number 15 has
binary representation 1111 and has no binary gaps. The number 32 has binary
representation 100000 and has no binary gaps.

Write a function:

    def solution(N)

that, given a positive integer N, returns the length of its longest binary gap.
The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary
representation 10000010001 and so its longest binary gap is of length 5.
Given N = 32 the function should return 0, because N has binary representation
'100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:
        N is an integer within the range [1..2,147,483,647].

'''
def solution(N):
    # using the "concept of bit manipulation" and "& operation"
    current_gap = 0
    max_gap = 0
    start_counting = False

    temp = N
    while temp > 0:
        # case 1
        if (temp & 1 == 1):
            # case 1-1
            if (start_counting == False):
                start_counting = True
            # case 1-2
            elif (start_counting == True):
                max_gap = max(max_gap, current_gap)
                current_gap = 0 #reset

        # case 2
        elif (temp & 1 == 0):
            if(start_counting == True):
                current_gap += 1

        # shift one bit (every loop)
        temp = temp >> 1

    return max_gap
