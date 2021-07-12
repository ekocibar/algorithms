"""
https://www.hackerrank.com/challenges/greedy-florist
"""

def getMinimumCost(k, c):
    c.sort(reverse=True)
    total_cost = 0
    for index, cost in enumerate(c):
        total_cost += ((index//k) + 1) * cost
    return total_cost

