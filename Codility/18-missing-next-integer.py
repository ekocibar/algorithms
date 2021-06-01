'''
Write a function:

    def solution(A)

that, given an array A of N integers, returns the smallest positive integer
(greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

-N is an integer within the range [1..100,000];
-each element of array A is an integer within the range [−1,000,000..1,000,000]-
'''
def solution(A):
    if (len(A) == 0) or (max(A) < 1):
        return 1
    for num in range(1, max(A)+2):
        if not num in A:
            return num

# solution([])
# solution([1,2,4,4,5,5])
solution([1, 2, 3])
# solution([3])
# solution([-1])
