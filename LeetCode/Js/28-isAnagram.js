// https://leetcode.com/problems/valid-anagram

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
 const isAnagram = (s, t) => {
  let hashS = {}
  let hashT = {}

  for (let char of s) hashS[char] = (hashS[char] || 0) + 1
  for (let char of t) hashT[char] = (hashT[char] || 0) + 1

  if (Object.keys(hashS).length != Object.keys(hashT).length) return false

  for (let key of Object.keys(hashS)) {
      if (hashS[key] != hashT[key])  return false
  }

  return true

}

// const isAnagram = (s, t) => {
//     let a = s.split('').sort((a, b) => a > b ? 1 : -1).join()
//     let b = t.split('').sort((a, b) => a > b ? 1 : -1).join()

//     return a === b
// }
