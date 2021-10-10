// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

/**
 * @param {number[]} prices
 * @return {number}
 */
const maxProfit = (prices) => {
  let profit = 0
  for (let i=1; i<  prices.length; i++) {
    if (prices[i] > prices[i-1]){
        profit += prices[i] - prices[i-1]
    }
  }
  return profit
}


// One liner
const maxProfit = (prices) => prices.reduce(
  (total, price, index) => (index > 0 && price > prices[index - 1])
    ? total + price - prices[index - 1]
    : total, 0)
