//  https://leetcode.com/problems/group-anagrams

/**
 * @param {string[]} strs
 * @return {string[][]}
 */
 var groupAnagrams = function(strs) {
  if (strs === [""]) return [[""]]

  let hash = {}
  let sortedStr
  for (let str of strs) {
      sortedStr = str.split('').sort((a, b) => a > b ? 1 : -1).join('')
      hash[sortedStr] ? hash[sortedStr] = [...hash[sortedStr], str] : hash[sortedStr] = [str]

      // Longer and Safer
      // if(!hash.hasOwnProperty(sortedStr)) {
      //     hash[sortedStr] = [str]
      // } else {
      //     hash[sortedStr] = [...hash[sortedStr], str]
      // }

  }
  return Object.values(hash)
}