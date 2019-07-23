class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value == self.value or self.value is None:
      self.value = value

    elif value < self.value:
      if self.left is None:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)

    else: # value > self.value:
      if self.right is None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value is None or self.value == target:
      return True # return self.value

    if self.value < target:
      self.value = self.left
      return contains(target)

  def get_max(self):
    pass

  def for_each(self, cb):
    pass