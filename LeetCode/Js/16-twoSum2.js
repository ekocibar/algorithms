// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
 const twoSum = (numbers, target) => {
    let hash = {}

    for(let i=0; i<numbers.length; i++) {
      if (numbers[i] in hash) return [hash[numbers[i]], i+1]
      hash[target-numbers[i]] = i + 1
    }
}
