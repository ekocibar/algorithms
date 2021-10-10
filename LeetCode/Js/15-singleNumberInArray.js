// https://leetcode.com/problems/single-number

/**
 * @param {number[]} nums
 * @return {number}
 */
 const singleNumber = (nums) => {
  let hash = {}
  for(let num of nums) {
      num in hash ? hash[num]=2 : hash[num]=1
  }
  for (let key in hash) {
      if(hash[key] === 1) return key
  }
}
