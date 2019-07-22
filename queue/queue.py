class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = [] # list or array

  # add item to back of queue
  def enqueue(self, item):
    self.storage.append(item)
    self.size+=1
  
  # remove and return an item from the front of the queue
  # return none if size = 0
  def dequeue(self):
    if self.size == 0:
      return None

    self.size-=1
    return self.storage.pop(0)

  # returns the number of items in the queue
  def len(self):
    return self.size
