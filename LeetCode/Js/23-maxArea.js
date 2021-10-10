// https://leetcode.com/problems/container-with-most-wate

/**
 * @param {number[]} heights
 * @return {number}
 */
 var maxArea = function(heights) {
  let maxArea = 0
  let left = 0
  let right = heights.length - 1
  let currentArea

  while( left < right) {
      currentArea = Math.min(heights[left], heights[right]) * (right - left)
      maxArea = Math.max(maxArea, currentArea)

      if (heights[left] > heights[right]){
          right--
      } else {
          left++
      }
  }
  return maxArea
}
