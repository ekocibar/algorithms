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
