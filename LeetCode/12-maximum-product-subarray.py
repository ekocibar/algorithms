'''https://leetcode.com/problems/maximum-product-subarray/
Given an integer array nums, find a contiguous non-empty subarray within the
array that has the largest product, and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.



Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.



Constraints:

    1 <= nums.length <= 2 * 104
    -10 <= nums[i] <= 10
    The product of any prefix or suffix of nums is guaranteed to fit in a
    32-bit integer.

'''
def maxProduct(nums):
    max_prod, min_prod, ans = nums[0], nums[0], nums[0]
    for i in range(1, len(nums)):
        x = max(nums[i], max_prod*nums[i], min_prod*nums[i])
        y = min(nums[i], max_prod*nums[i], min_prod*nums[i])
        max_prod, min_prod = x, y
        ans = max(max_prod, ans)
    return ans

# Kodane
def maxProduct(nums) :
    prefix, suffix, max_so_far = 0, 0, float('-inf')
    for i in range(len(nums)):
        prefix = (prefix or 1) * nums[i]
        suffix = (suffix or 1) * nums[-i]
        max_so_far = max(max_so_far, prefix, suffix)
    return max_so_far

maxProduct([1,3,-1, 5])


# Second way
def maxProduct2(A):
    B = A[::-1]
    for i in range(1, len(A)):
        A[i] *= A[i - 1] or 1
        B[i] *= B[i - 1] or 1
    return max(A + B)

maxProduct2([1,3,-1, 5])
