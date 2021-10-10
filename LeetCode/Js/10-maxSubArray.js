// https://leetcode.com/problems/maximum-subarray/

/**
 * @param {number[]} nums
 * @return {number}
 */
 const maxSubArray = (nums) => {
  // empty array
  if (!nums) return 0

  // All negative
  if (Math.max(nums) < 0) return Math.max(nums)

  // set min value of total
  let globalMax = nums[0]
  let currentMax = nums[0]

  for (let i=1; i<nums.length; i++) {
    // Maximum till index i
    currentMax = Math.max(currentMax + nums[i], nums[i])

    // Store global max
    globalMax = Math.max(globalMax, currentMax)
  }

  return globalMax
}