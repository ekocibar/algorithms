// https://leetcode.com/problems/product-of-array-except-self/


/** 6 * @param {number[]} nums
 * @return {number}
 */
const getProduct = (nums) => nums.reduce((acc, num) => acc*num, 1)

/**
 * @param {number[]} nums
 * @return {number[]}
 */
 const productExceptSelf = (nums) => {
  const productOfAll = getProduct(nums)
  return nums.map((num, index) => num===0 ? getProduct([...nums].filter((num, idx) => idx != index)) : productOfAll/num)
}
