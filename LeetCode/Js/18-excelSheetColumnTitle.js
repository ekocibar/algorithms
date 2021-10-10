// https://leetcode.com/problems/excel-sheet-column-title

/**
 * @param {number} columnNumber
 * @return {string}
 */
 const convertToTitle = (n) => {
  let newStr = "";
  while(n > 0){
      n--
      let charCode = String.fromCharCode((n % 26) + 65)
      newStr = charCode + newStr
      n = Math.floor(n/ 26)
  }

  return newStr
}
