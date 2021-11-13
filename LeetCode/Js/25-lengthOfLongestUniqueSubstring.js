// https://leetcode.com/problems/longest-substring-without-repeating-characters

/**
 * @param {string} s
 * @return {number}
 */
 var lengthOfLongestSubstring = function(s) {

  let currentLength = 0
  let maxLength = 0
  let currentStack = []

  for(let letter of s) {
      indexOf = currentStack.indexOf(letter)
      // letter is not in the stack
      if (indexOf === -1){
          currentStack.push(letter)
          currentLength++
      }
      //  letter is  in the stack
      else {
          currentStack = currentStack.slice(indexOf + 1)
          currentStack.push(letter)
          currentLength = currentStack.length
      }
      maxLength = Math.max(maxLength, currentLength)
  }
  return maxLength
}
