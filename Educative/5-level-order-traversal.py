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
