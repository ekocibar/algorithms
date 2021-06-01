# 9. How many ways can you make change with coins and a total amount
'''Suppose we have coin denominations of [1, 2, 5] and the total amount is 7.
We can make changes in the following 6 ways:
Denominations 1,2,5
Amount 7

1,1,1,1,1,1,1
1,1,1,1,1,2
1,1,1,2,2
1,2,2,2
1,1,5
2,5

Total Methods
'''
def solve_coin_change(denominations, amount):
  total_ways_list = [0] * (amount + 1)
  total_ways_list[0] = 1
  # print(total_ways_list)
  for den in denominations:
    for i in range(den, amount + 1):
      total_ways_list[i] += total_ways_list[i - den]

  return total_ways_list[len(total_ways_list) - 1]

solve_coin_change([1,2,5], 7)
