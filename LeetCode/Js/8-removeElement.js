// https://leetcode.com/problems/remove-element

/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
 const removeElement = (nums, val) => {
  for (i = 0; i < nums.length; i++) {
      if (nums[i] == val) {
          nums.splice(i, 1);
          i--;
      }
  }
}
