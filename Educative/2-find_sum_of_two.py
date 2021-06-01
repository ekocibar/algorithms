# 2. Determine if the sum of two integers is equal to the given value
'''Given an array of integers and a value, determine if there
are any two integers in the array whose sum is equal to the
given value. Return true if the sum exists and return false
if it does not. Consider this array and the target sums:'''
def find_sum_of_two(A, val):
    d = {}
    for num in A:
        d[num] = True
    for i, num in enumerate(A):
        target = val - num
        if d.get(target) and (target in A[:i] or target in A[i+1:]):
            return True
    return False

# Another approach
def find_sum_of_two2(A, val):
  for idx, number in enumerate(A):
    if val - number in A[:idx] + A[idx+1:]:
      return True
  return False