class Heap:
  def __init__(self, comparator):
    self.storage = []
    self.comparator = comparator

  def insert(self, value):
    pass

  def delete(self):
    pass

  def get_priority(self):
    pass

  def get_size(self):
    pass

  """moves the element at the specified index "up" the heap by swapping it with its parent if the parent's value is less than the value at the specified index (if parent < child, swap )."""
  
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
