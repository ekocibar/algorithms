// https://leetcode.com/problems/longest-common-prefix

/**
 * @param {string[]} strs
 * @return {string}
 */
 var longestCommonPrefix = function(strs) {
  if(!strs) return ''
  let longest = strs[0]
  for(let i=1; i<strs.length; i++) {
      let lastCommonIndex = 0
      let limit = Math.min(longest.length, strs[i].length)
      for(let j=0; j<=limit; j++){
          if(strs[i][j] == longest[j]) lastCommonIndex++
          if (lastCommonIndex == 0) return ''
          if(strs[i][j] != longest[j]) {
              longest = longest.substring(0, lastCommonIndex)
          }
      }
  }
return longest
}
