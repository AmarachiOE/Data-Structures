"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next) # wrapping
    if current_next: # if current item already has next item
      current_next.prev = self.next # inserting this next value before (prev) the new items "current_next"

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""

# LL = (doubly) linked list
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    new_node = ListNode(value, None, next=self.head)

    if self.head == None: # our LL is empty
      self.head = new_node
      self.tail = new_node

    else: # LL is not empty
      self.head.insert_before(value)
      self.head = new_node

    self.length += 1

  def remove_from_head(self):
    
    removed = self.head
    if self.length <= 1:
      self.head = None
      self.tail = None
      self.length = 0

    else:
      self.head = self.head.next
      self.head.prev.delete()
      self.length -= 1

    return removed.value

  def add_to_tail(self, value):
    new_node = ListNode(value, prev=self.tail)
    
    if self.head == None:
      self.head = new_node
      self.tail = new_node

    else:
      self.tail.insert_after(value)
      self.tail = new_node

    self.length += 1

  def remove_from_tail(self):

    removed = self.tail
    if self.length <= 1:
      self.head = None
      self.tail = None
      self.length = 0

    else:
      self.tail = self.tail.prev
      self.tail.next.delete()
      self.length -= 1

    return removed.value


  def move_to_front(self, node):
    # moved_node = node # save copy of node
    # node.delete() # delete original
    # moved_node.prev = None
    # moved_node.next = self.head
    # self.head = moved_node
    self.add_to_head(node.value)
    self.delete(node)


  def move_to_end(self, node):
    self.add_to_tail(node.value)
    self.delete(node) # delete original reference to node


    """
    Working
    if node == self.head:
      self.head = self.head.next
      
    
    if self.length > 1 and node != self.tail:
      self.tail.insert_after(node.value)
      self.tail = self.tail.next
    """
    


  def delete(self, node):
    if self.length <= 1:
      self.head = None
      self.tail = None
      self.length = 0
    
    elif node == self.head:
      self.head = self.head.next
      self.head.prev.delete()
      self.length -= 1

    elif node == self.tail:
      self.tail = self.tail.prev
      self.tail.next.delete()
      self.length -= 1

    else:
      node.delete()
      self.length -= 1

    
    
  
    
  def get_max(self):
    current = self.head
    max = 0

    while current:
      # if current.value is None:
      #   return max

      if current.value > max:
        max = current.value

      current = current.next

    return max
