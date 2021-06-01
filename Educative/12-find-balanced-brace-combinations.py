# 12. Print balanced brace combinations
'''Print all braces combinations for a given value n so that they are balanced.
For this solution, we will be using recursion. For n = 3 :
[
  ['{', '{', '{', '}', '}', '}'],
  ['{', '{', '}', '{', '}', '}'],
  ['{', '{', '}', '}', '{', '}'],
  ['{', '}', '{', '{', '}', '}'],
  ['{', '}', '{', '}', '{', '}']
]
'''
import copy

def print_all_braces_rec(n, left_count, right_count, output, result):

  if left_count >= n and right_count >= n:
    result.append(copy.copy(output))

  if left_count < n:
    output += '{'
    print_all_braces_rec(n, left_count + 1, right_count, output, result)
    output.pop()

  if right_count < left_count:
    output += '}'
    print_all_braces_rec(n, left_count, right_count + 1, output, result)
    output.pop()

def print_all_braces(n):
  output = []
  result = []
  print_all_braces_rec(n, 0, 0, output, result)
  return result


''' From StackOverflow
This problem boils down to 3 different cases:

1. We've used all of our open parentheses and just need to close them
2. We don't have any currently open parentheses and need to add one before closing again
3. We've got at least one open and can either open a new one or close one.

To follow that logic, we then need to keep track of the number of open parens
we have left to use (no below), the current string of parens, and the current
balance of open vs. closed (curb below):'''
def parens(no, s="", curb=0):
  # case 1: all open parens used
  if no == 0:
    if curb == 0:
      return [s]
    return parens(no, s+")", curb-1)

  # case 2: none are currently open
  if curb == 0:
    return parens(no-1, s+"(", curb+1)

  # case 3: one or more are currently open
  return parens(no-1, s+"(", curb+1) + parens(no, s+")", curb-1)