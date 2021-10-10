// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

/**
 * @param {number[]} prices
 * @return {number}
 */
 const maxProfit = (prices) => {
  let globalMaxProfit = 0
  let currentBestBuy = prices[0]

  for (let price of prices) {
    currentBestBuy = Math.min(currentBestBuy, price)
    globalMaxProfit = Math.max(globalMaxProfit, price - currentBestBuy)
  }
  return globalMaxProfit
}
