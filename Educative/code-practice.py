# SOURCE: https://www.educative.io/blog/crack-amazon-coding-interview-questions#questions


# 1. Find the missing number in the array
'''You are given an array of positive numbers from 1 to n,
such that all numbers from 1 to n are present except one number x.
You have to find x. The input array is not sorted. Look at the
below array and give it a try before checking the solution.'''
def find_missing(input):
  n = len(input) +1
  sum_array = sum(input)
  sum_included_missing = (n*(n+1))/2
  missing_element = sum_included_missing - sum_array

  return int(missing_element)


# 2. Determine if the sum of two integers is equal to the given value
'''Given an array of integers and a value, determine if there
are any two integers in the array whose sum is equal to the
given value. Return true if the sum exists and return false
if it does not. Consider this array and the target sums:'''
def find_sum_of_two(A, val):
  for idx, number in enumerate(A):
    if val- number in A[:idx] + A[idx+1:]:
      return True
  return False


# 3. Merge two sorted linked lists
'''Given two sorted linked lists, merge them so that the
resulting linked list is also sorted. Consider two sorted
linked lists and the merged list below them as an example.'''
def merge_sorted(head1, head2):
  # if both lists are empty then merged list is also empty
  # if one of the lists is empty then other is the merged list
  if head1 == None:
    return head2
  elif head2 == None:
    return head1

  mergedHead = None
  if head1.data <= head2.data:
    mergedHead = head1
    head1 = head1.next
  else:
    mergedHead = head2
    head2 = head2.next

  mergedTail = mergedHead

  while head1 != None and head2 != None:
    temp = None
    if head1.data <= head2.data:
      temp = head1
      head1 = head1.next
    else:
      temp = head2
      head2 = head2.next

    mergedTail.next = temp
    mergedTail = temp

  if head1 != None:
    mergedTail.next = head1
  elif head2 != None:
    mergedTail.next = head2

  return mergedHead


# 4. Copy linked list with arbitrary pointer
'''You are given a linked list where the node has two pointers.
The first is the regular next pointer. The second pointer is called
arbitrary_pointer and it can point to any node in the linked list.
Your job is to write code to make a deep copy of the given linked list.
Here, deep copy means that any operations on the original list should
not affect the copied list.'''
def deep_copy_arbitrary_pointer(head):
  if head == None:
    return None

  current = head
  new_head = None
  new_prev = None
  ht = dict()

  # create copy of the linked list, recording the corresponding
  # nodes in hashmap without updating arbitrary pointer
  while current != None:
    new_node = LinkedListNode(current.data)

    # copy the old arbitrary pointer in the new node
    new_node.arbitrary = current.arbitrary;

    if new_prev != None:
      new_prev.next = new_node
    else:
      new_head = new_node

    ht[current] = new_node

    new_prev = new_node
    current = current.next

  new_current = new_head

  # updating arbitrary pointer
  while new_current != None:
    if new_current.arbitrary != None:
      node = ht[new_current.arbitrary]

      new_current.arbitrary = node

    new_current = new_current.next

  return new_head


# 5. Level Order Traversal of Binary Tree
'''Given the root of a binary tree, display the node values at each level.
Node values for all levels should be displayed on separate lines. Let’s take a
look at the below binary tree.'''
# Using two queues
def level_order_traversal(root):
  if root == None:
    return
  result = ""
  queues = [deque(), deque()]

  current_queue = queues[0]
  next_queue = queues[1]

  current_queue.append(root)
  level_number = 0

  while current_queue:
    temp = current_queue.popleft()
    result += str(temp.data) + " "

    if temp.left != None:
      next_queue.append(temp.left)

    if temp.right != None:
      next_queue.append(temp.right)

    if not current_queue:
      level_number += 1
      current_queue = queues[level_number % 2]
      next_queue = queues[(level_number + 1) % 2]
  return result


# 6. Determine if a binary tree is a binary search tree
'''Given a Binary Tree, figure out whether it’s a Binary Search Tree. In a
binary search tree, each node’s key value is smaller than the key value of all
nodes in the right subtree, and is greater than the key values of all nodes in
the left subtree. Below is an example of a binary tree that is a valid BST.'''
import sys
def is_bst_rec(root, min_value, max_value):
  if root == None:
    return True

  if root.data < min_value or root.data > max_value:
    return False

  return is_bst_rec(root.left, min_value, root.data) and is_bst_rec(root.right, root.data, max_value)

def is_bst(root):
  return is_bst_rec(root, -sys.maxint - 1, sys.maxint)


# 7. String segmentation
'''You are given a dictionary of words and a large input string. You have to
find out whether the input string can be completely segmented into the words of
a given dictionary. The following two examples elaborate on the problem further.
Given a dictionary of words.
apple apple pear pie
Input string of “applepie” can be segmented into dictionary words.
Input string “applepeer” cannot be segmented into dictionary words.'''
def can_segment_string(s, dictionary):
  for i in range(1, len(s)+1):
    first_part = s[:i]
    if first_part in dictionary:
      second_part = s[i:]
      if not second_part or second_part in dictionary\
        or can_segment_string(second_part,dictionary):
        return True
  return False


# 8. Reverse Words in a Sentence
'''Reverse the order of words in a given sentence (an array of characters).
"Hello World"  >>   "World Hello"'''
def reverse_words(sentence):
  list_of_words = sentence.split()
  return ' '.join(list_of_words[::-1])
reverse_words('We love Python')

# Solution of website
def str_rev(str, start, end):
  if str == None or len(str) < 2:
    return

  while start < end:
    temp = str[start]
    str[start] = str[end]
    str[end] = temp

    start += 1
    end -= 1
  return str

def reverse_words(sentence):

  # Here sentence is a null-terminated string ending with char '\0'.

  if sentence == None or len(sentence) == 0:
    return

  #  To reverse all words in the string, we will first reverse
  #  the string. Now all the words are in the desired location, but
  #  in reverse order: "Hello World" -> "dlroW olleH".

  str_len = len(sentence)
  sentence = str_rev(sentence, 0, str_len - 2)

  # Now, let's iterate the sentence and reverse each word in place.
  # "dlroW olleH" -> "World Hello"

  start = 0
  end = 0

  while True:

  # find the  start index of a word while skipping spaces.
    while start < len(sentence) and sentence[start] == ' ':
      start += 1

    if start == str_len:
      break

  # find the end index of the word.
    end = start + 1
    while end < str_len and sentence[end] != ' ' and sentence[end] != '\0':
      end += 1

  # let's reverse the word in-place.
    sentence = str_rev(sentence, start, end - 1)
    start = end
  return sentence


# 9. How many ways can you make change with coins and a total amount
'''Suppose we have coin denominations of [1, 2, 5] and the total amount is 7.
We can make changes in the following 6 ways:
Denominations 1,2,5
Amount 7

1,1,1,1,1,1,1
1,1,1,1,1,2
1,1,1,2,2
1,2,2,2
1,1,5
2,5

Total Methods
'''
def solve_coin_change(denominations, amount):
  solution = [0] * (amount + 1)
  solution[0] = 1
  # print(solution)
  for den in denominations:
    for i in range(den, amount + 1):
      solution[i] += solution[i - den]

  return solution[len(solution) - 1]

solve_coin_change([1,2,5], 7)


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

# WEBSITE SOLUTION
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

''' StackOverflow
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
