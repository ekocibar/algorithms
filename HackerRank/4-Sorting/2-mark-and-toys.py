"""
https://www.hackerrank.com/challenges/mark-and-toys
"""
def maximumToys(prices, k):
    prices.sort()
    count = 0
    cumulative_sum = 0
    for price in prices:
        cumulative_sum += price
        if cumulative_sum <= k:
            count += 1
        else:
            break
    return count
