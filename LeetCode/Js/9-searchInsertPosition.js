// https://leetcode.com/problems/search-insert-position

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
 const searchInsert = (nums, target) => {
  if (target <= nums[0]) return 0

  for (i in nums) {
      if (nums[i] >= target){
          return i
      }
  }
  return nums.length
}
