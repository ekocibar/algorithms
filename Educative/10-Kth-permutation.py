
# 10. Find Kth permutation
'''Given a set of ‘n’ elements, find their Kth permutation.
Consider the following set of elements:
1 2 3
All permutations of the above elements are (with ordering):
1 123
2 132
3 213
4 231
5 312
6 321
'''
def factorial(n):
  if n == 0 or n == 1:
    return 1
  return n * factorial(n -1 )

def find_kth_permutation(v, k, result):
  if not v:
    return

  n = len(v)
  # count is number of permutations starting with first digit
  count = factorial(n - 1)
  selected = (k - 1) // count

  result += str(v[selected])
  del v[selected]
  k = k - (count * selected)
  find_kth_permutation(v, k, result)
