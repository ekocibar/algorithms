"""
https://www.hackerrank.com/challenges/new-year-chaos
"""

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimum_bribes(q):
    bribes = 0
    q = [i-1 for i in q]
    for i, o in enumerate(q):
        cur = i

        if o - cur > 2:
            print("Too chaotic")
            return

        for k in q[max(o - 1, 0):i]:
            if k > o:
                bribes += 1

    print(bribes)



minimumBribes([1,2,5,3,4,7,8,6])
