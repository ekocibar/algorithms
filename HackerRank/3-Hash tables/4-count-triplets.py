"""
https://www.hackerrank.com/challenges/count-triplets-1
"""


from collections import defaultdict


def count_triplets(arr, r):
    arr2 = defaultdict(int)
    arr3 = defaultdict(int)
    count = 0
    for i in arr:
        count += arr3[i]
        arr3[i*r] += arr2[i]
        arr2[i*r] += 1

        print(f'arr2 = {arr2} -- arr3 = {arr3} -- count = {count}')
    return count


count_triplets([1,2,2,2,4,5,8], 2)
'''
arr2 = {1: 0, 2: 1}                             -- arr3 = {1: 0, 2: 0}                          -- count = 0
arr2 = {1: 0, 2: 1, 4: 1}                       -- arr3 = {1: 0, 2: 0, 4: 1}                    -- count = 0
arr2 = {1: 0, 2: 1, 4: 2}                       -- arr3 = {1: 0, 2: 0, 4: 2}                    -- count = 0
arr2 = {1: 0, 2: 1, 4: 3}                       -- arr3 = {1: 0, 2: 0, 4: 3}                    -- count = 0
arr2 = {1: 0, 2: 1, 4: 3, 8: 1}                 -- arr3 = {1: 0, 2: 0, 4: 3, 8: 3}              -- count = 3
arr2 = {1: 0, 2: 1, 4: 3, 8: 1, 5: 0, 10: 1}    -- arr3 = {1: 0, 2: 0, 4: 3, 8: 3, 5: 0, 10: 0} -- count = 3
arr2 = {1: 0, 2: 1, 4: 3, 8: 1, 5: 0, 10: 1, 16: 1} -- arr3 = {1: 0, 2: 0, 4: 3, 8: 3, 5: 0, 10: 0, 16: 1} -- count = 6
'''