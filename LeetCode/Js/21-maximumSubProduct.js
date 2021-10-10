// https://leetcode.com/problems/maximum-product-subarray

/**
 * @param {number[]} nums
 * @return {number}
 */
 const maxProduct = (nums) => {

  let currentMax = nums[0]
  let currentMin = nums[0]
  let globalMax = nums[0]

  for (let i=1; i<nums.length; i++) {
      let num = nums[i]
      // Get currents
      x = Math.max(num, currentMax*num, currentMin*num)
      y = Math.min(num, currentMax*num, currentMin*num)
      currentMax = x
      currentMin = y

      // Get global max
      globalMax =  Math.max(currentMax, globalMax)
  }

  return globalMax
}
