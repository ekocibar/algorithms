// https://leetcode.com/problems/excel-sheet-column-number/

/**
 * @param {string} columnTitle
 * @return {number}
 */
 const titleToNumber = (s) => s.split('').reduce((a, b) => a * 26 + b.charCodeAt(0) - 64, 0)
