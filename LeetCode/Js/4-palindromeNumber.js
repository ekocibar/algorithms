// https://leetcode.com/problems/palindrome-number

/**
 * @param {number} x
 * @return {boolean}
 */
 const isPalindrome = (x) => {
  if (x < 0) return false
  const strNum = '' + x
  const reversedStrNum = strNum.split('').reverse().join('')
  return strNum == reversedStrNum
};
