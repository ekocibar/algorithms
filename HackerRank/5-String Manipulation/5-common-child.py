"""
https://www.hackerrank.com/challenges/common-child
"""


def commonChild(s1, s2):
    prev = [0] * (len(s2)+1)
    curr = [0] * (len(s2)+1)

    for r in s1:
        for j, c in enumerate(s2, 1):
            curr[j] = prev[j-1] + 1 if r == c else max(prev[j], curr[j-1])
        prev, curr = curr, prev

    return prev[-1]

# ALTERNATIVE SOLUTION
def commonChild2(s1, s2):
  maxAt = {}

  for i1 in range(len(s1)):
    maxForI1 = 0
    for i2 in range(len(s2)):
        potentialSum = maxForI1 + 1

        other = maxAt.get(i2, 0)
        if other > maxForI1:
            maxForI1 = other

        if s1[i1] == s2[i2]:
            maxAt[i2] = potentialSum

  return max(maxAt.values(), default=0)
