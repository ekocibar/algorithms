"""
https://www.hackerrank.com/challenges/sock-merchant
"""

def sockMerchant(n, ar):
    def sockMerchant(n, ar):
    temp_pairs = {}
    num_pairs = 0
    for color in ar:
        if color in temp_pairs:
            if temp_pairs[color] == 1:
                num_pairs += 1
                temp_pairs[color] = 0
            else:
                temp_pairs[color] = 1
        else:
            temp_pairs[color] = 1
    return num_pairs
