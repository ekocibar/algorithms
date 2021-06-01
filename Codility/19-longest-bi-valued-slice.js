/*
Write a function:

    def solution(A)

that, given an array A of N integers, returns the length of the longest
bi-valued slice in A

For example, given A = [4, 2, 2, 4, 2], the function should return 5.

Given A = [1, 2, 3, 2], the function should return 3.

Given A = [−1, −3, 0, 5, 4, 4, 5, 12 ], the function should return 4.

Write an efficient algorithm for the following assumptions:

-N is an integer within the range [1..100];
-each element of array A is an integer within the range |1,000,000,000|
*/

function solution(A) {

    let biElements = new Set()
    let currentLength = 0
    let maxSliceLength = 0
    let consecutiveSequence = 1

    for(let i=0; i < A.length; i++){
        num = A[i]
        // Case 1 :
        // num is not in the biElements, and biElements has less than 2 values
        // > num should be added to biElements
        // > currentLength increases
        // > maxSliceLength should be updated
        if (!biElements.has(num) && biElements.size <  2){
            biElements.add(num)
            currentLength += 1
            maxSliceLength = Math.max(maxSliceLength, currentLength)
        }
        // Case 2:
        // num is not in the biElements, and biElements has already 2
        // > biElements should be updated with new value
        // > currentLength becomes previous consecutiveSequence + 1
        // > consecutiveSequesnce becomes 1 as biElements has a new value
        else if (!biElements.has(num) && biElements.size ==  2) {
            biElements = new Set([A[i-1], num])
            currentLength = consecutiveSequence + 1
            consecutiveSequence = 1
        }
        // Case 3:
        // num is in biElements
        // > currentLength increases
        // > maxSliceLength should be updated
        // > consecutiveSequence should be updated
        else {
            currentLength += 1
            maxSliceLength = Math.max(maxSliceLength, currentLength)
            consecutiveSequence = num === A[i-1] ? consecutiveSequence += 1 : 1
        }
    }

    return maxSliceLength
}
