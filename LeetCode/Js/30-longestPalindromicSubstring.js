// https://leetcode.com/problems/longest-palindromic-substring/

/**
 * @param {string} s
 * @return {string}
 */
 const longestPalindrome = (s) => {
  let longestSub = ''
  let lenLongestSub = 0
  let left, right
  for (let i = 0; i<s.length; i++) {
      left = i
      right = i
      while (left >= 0 && right < s.length && s[left] === s[right]) {
          if ((right - left + 1) > lenLongestSub){
              longestSub = s.slice(left, right + 1)
              lenLongestSub = right - left + 1
          }
          left--
          right++
      }
      left = i
      right = i + 1
      while (left >= 0 && right < s.length && s[left] === s[right]) {
          if ((right - left + 1) > lenLongestSub){
              longestSub = s.slice(left, right + 1)
              lenLongestSub = right - left + 1
          }
          left--
          right++
      }

  }
  return longestSub
}
