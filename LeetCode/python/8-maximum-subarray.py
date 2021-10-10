'''
Given an integer array nums, find the contiguous subarray (containing at least
one number) which has the largest sum and return its sum.


Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23



Constraints:

    1 <= nums.length <= 3 * 104
    -105 <= nums[i] <= 105


Follow up: If you have figured out the O(n) solution, try coding another
solution using the divide and conquer approach, which is more subtle
'''
def maxSubArray(nums):

    if max(nums) < 0:
        return max(nums)

    local_max_sum = nums[0]
    global_max_sum = nums[0]
    for index in range(1, len(nums)):
        local_max_sum = max(local_max_sum + nums[index], nums[index])
        print('lokal   >>  ', local_max_sum)
        global_max_sum = max(global_max_sum, local_max_sum)
        print('global   >>  ', global_max_sum)


    return global_max_sum


maxSubArray([1,2,-2,0,5,1])