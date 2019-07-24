"""
- Max Heap
- Root should be the maximum value (index = 0)
- Parent > children
"""

class Heap:
  def __init__(self):
    self.storage = []

  """ insert adds the input value into the heap; this method should ensure that the inserted value is in the correct spot in the heap"""
  def insert(self, value):
    # if array is empty, just add the value

    # add value to end
    self.storage.append(value) # added to end (last value and index)
    
    if len(self.storage) > 1: # so a list already existed before adding new value
      value_index = len(self.storage)-1 # grab index of last added item
      self._bubble_up(value_index)
      print("Bubble Up called")

    """
    # if array is empty, just add the value
    if len(self.storage) == 0:
      self.storage.append(value)

    # check if value is greater than the root/max value at [0]
    # if it is, insert value at [0]
    # added new (needed??): if len(storage) = 1
    if len(self.storage) == 1: # is this line needed?
      if value > self.storage[0]:
        self.storage.insert(0, value)



    

    # or check if the value < root:
    if value < self.storage[0]:
      # if root is only element in list:
      # add value to end
      if len(self.storage) == 1:
        self.storage.append(value)
      
      # 1. or if there's > 1 element in the list
      # 2. while loop with increment and recursion
      # for each element check: 
      
      # i = 0
      # while i in range(0, len(self.storage)-1): # leave out last 1? 
      
      # parent = self.storage[i]
      # left_child = self.storage[2i+1]
      # right_child = self.storage[2i+2]
      # if value is > element's left child
      # if value is < element's right child
      # if value > left and value < right, insert
      # then i += 1
      
      
      elif len(self.storage) > 1:
        # for i in range(0, len(self.storage)):
        #   left_child = self.storage[2i+1]
        i = 0
        while i in range(0, len(self.storage)-1):
          parent = self.storage[i]
          left_child = self.storage[2i+1]
          right_child = self.storage[2i+2]
          if value > parent and value > left_child and value < right_child


    else:

      for i in range(0, len(self.storage)):
        if value > self.storage[i] and value < self.storage[i+1]:
          self.storage.insert(i, value)
    """


  def delete(self):
    pass

  def get_max(self):
    pass

  def get_size(self):
    pass

  """ _bubble_up moves the element at the specified index "up" the heap by swapping it with its parent if the parent's value is less than the value at the specified index (if parent < child, swap )."""
  def _bubble_up(self, index):
    while index > 0:
      # identify parent
      parent = (index - 1) // 2

      # compare: if child is greater than parent
      if self.storage[index] > self.storage[parent]:
        # swap
        # so this is a max heap since we want the higher value on top
        self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]

        # now update the index (change node so while loop can keep going)
        index = parent

      else:
          break

  def _sift_down(self, index):
    pass
