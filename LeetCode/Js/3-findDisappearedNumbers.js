// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array

/**
 * @param {number[]} nums
 * @return {number[]}
 */
 const findDisappearedNumbers = function(nums) {
  let supposedNumbers = []
  for (let i=1;i<=nums.length;i++){
      supposedNumbers.push(i)
  }
  const disappearedNumbers = supposedNumbers.filter((num) => !nums.includes(num))
  return disappearedNumbers
}