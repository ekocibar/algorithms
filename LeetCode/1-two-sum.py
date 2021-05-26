'''
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]



Constraints:

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) ?
'''

# Brute Force
def twoSum(nums, target):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

# Hash table approach
def twoSum2(nums, target):
    seen = {}
    for index, num in enumerate(nums):
        other = target - num

        if other in seen:
            return [seen[other], index]
        else:
            seen[num] = index

# Hash table approach 2
def twoSum3(nums, target):
    the_dic = {}
    length = len(nums)

    # Make {value1: index1, value2 : index2,....}  also {nums[i] : i,.....}
    for i in range(length):
        the_dic[nums[i]] = i

    for i in range(length):
        remain = target - nums[i]
        found = the_dic.get(remain) # get(): to check if the key exist

        if found and (i!=found):  # make sure not selected the same index
            return [ i, found ]
