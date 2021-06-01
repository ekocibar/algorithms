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