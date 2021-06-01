'''
Write a function:

    def solution(A)

that, given an array A of N integers, returns the length of the longest
bi-valued slice in A

For example, given A = [4, 2, 2, 4, 2], the function should return 5.

Given A = [1, 2, 3, 2], the function should return 3.

Given A = [−1, −3, 0, 5, 4, 4, 5, 12 ], the function should return 4.

Write an efficient algorithm for the following assumptions:

-N is an integer within the range [1..100];
-each element of array A is an integer within the range [−1,000,000..1,000,000]-
'''
def solution(A):
    bi_elements = set()
    current_length = 0
    max_slice_length = 0
    consecutive_sequence = 1

    for i in range(len(A)):
        num = A[i]
        if not (num in bi_elements) and len(bi_elements) < 2:
            bi_elements.add(num)
            current_length += 1
            max_slice_length = max(max_slice_length, current_length)

        elif (not (num in bi_elements)) and (len(bi_elements) == 2):
            bi_elements = {A[i-1], num}
            current_length = consecutive_sequence + 1
            consecutive_sequence = 1

        else:
            current_length += 1
            max_slice_length = max(max_slice_length, current_length)

            if num == A[i-1]:
                consecutive_sequence += 1
            else:
                consecutive_sequence = 1

    return max_slice_length

