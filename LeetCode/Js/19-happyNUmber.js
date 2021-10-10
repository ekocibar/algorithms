// https://leetcode.com/problems/happy-number

/**
 * @param {number} n
 * @return {boolean}
 */
 var isHappy = function(n) {
  const originalNum = n
  const foundNums = [n]
  while(true){
      n = n.toString().split('').reduce((acc,num) => acc + Number(num) ** 2, 0)
      if (n===1) return true
      if (n===originalNum || foundNums.includes(n)) return false
      foundNums.push(n)
  }
}
