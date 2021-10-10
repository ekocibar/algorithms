/**
 *
 *
  Input: nums = [0,0,1,1,1,2,2,3,3,4]
  Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
 const removeDuplicates = nums => {
    // original length
    const originalArrayLength = nums.length;

    // length of uniques
    const uniques = [...new Set(nums)].sort()
    const uniquesSize = uniques.length

    // remaining part with "_"
    const duplicates = Array(originalArrayLength - uniquesSize).fill('_')

    return [...uniques, ...duplicates ]
}