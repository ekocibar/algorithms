# 11. Find all subsets of a given set of integers
'''We are given a set of integers and we have to find all the possible subsets
of this set of integers. The following example elaborates on this further.

Given set of integers:
2 3 4
All possile subsets for the given set of integers:
- 2 3 2, 3 4 2, 4 3, 4 2, 3, 4
'''

def get_all_subsets(s):
  x = len(s)
  list_of_subsets = []
  for i in range(2**x):
    list_of_subsets.append(set([s[j] for j in range(x) if (i & (2**j))]))
  return list_of_subsets

get_all_subsets([1,3,5])

# Another approach
def get_bit(num, bit):
    temp = (1 << bit)
    temp = temp & num
    if temp == 0:
      return 0
    return 1

def get_all_subsets(v, sets):
    subsets_count = 2 ** len(v)
    for i in range(0, subsets_count):
      st = set([])
      for j in range(0, len(v)):
         if get_bit(i, j) == 1:
            st.add(v[j])
      sets.append(st)
