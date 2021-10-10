// https://leetcode.com/problems/two-sum/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 const twoSum = function(nums, target) {

    hash = {}
    for (let i=0; i<nums.length; i++) {
        if(hash.hasOwnProperty(nums[i])){
            return [hash[nums[i]], i]
        } else {
            hash[target-nums[i]] = i
        }
    }
}
