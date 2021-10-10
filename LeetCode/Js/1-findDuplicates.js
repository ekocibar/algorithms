// https://leetcode.com/problems/find-all-duplicates-in-an-array/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
 const findDuplicates = function(nums) {
  let hash = {}
  let duplicatedNumbers = []
  for (let num of nums){
        if(!hash.hasOwnProperty(num)){
            hash[num] = true
        } else{
            duplicatedNumbers.push(num)
        }
    }
    return duplicatedNumbers
}
