"""
https://www.hackerrank.com/challenges/ctci-ice-cream-parlor
"""

def whatFlavors(cost, money):
    saved = {}
    for i,n in enumerate(cost):
        if money-n in saved:
            print(saved[money-n], i+1)
        saved[n] = i+1
