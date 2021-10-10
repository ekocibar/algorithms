// https://leetcode.com/problems/3sum

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
 const threeSum =(nums)  => {
  let res = {}
  const map = nums.reduce((acc, num, index) => {
      acc[num] = index
      return acc
  }, {})

  for( let i = 0; i < nums.length; i++) {
      for( let j = i+1; j < nums.length; j++){
          const num1 = nums[i]
          const num2 = nums[j]
          const num3 = -(num1 + num2)

          if( map[num3] && map[num3] != i && map[num3] != j){
              const triplet = [num1, num2, num3].sort((a,b) => a-b)
              if(!res[triplet]) {
                  res[triplet] = triplet
              }
          }
      }
  }

  return Object.values(res)
}