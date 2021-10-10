// https://leetcode.com/problems/plus-one

/**
 * @param {number[]} digits
 * @return {number[]}
 */
 const plusOne = (digits) => {
  // Start from last to first
  for (i = digits.length - 1; i>=0; i--){
      // Current digit is 9 make it 0 and continue looping.
      if(digits[i] === 9){
          digits[i] = 0
      }
      // Current digit isn't 9, so inrease the current by 1 and return the array.
      // e.g. 2199 would be 2200
      else {
          digits[i]++
          return digits
      }
  }
  // If the loop didnt stopped that means all the numbers are 9,
  // so add 1 at the beginning of the array.
  // Note: All "9"s are convered to 0 above. So 999 would be 1000
  return [1, ...digits]
}
