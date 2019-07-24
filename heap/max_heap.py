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
        # append value to end of list (last index)
        self.storage.append(value)

        # If list items already existed before adding new value
        if len(self.storage) > 1:
            # grab index of last added item
            value_index = len(self.storage)-1

            # pass index into bubble_up()
            self._bubble_up(value_index)
            # print("Bubble Up called")

    """ delete removes and returns the 'topmost' value from the heap; this method needs to ensure that the heap property is maintained after the topmost element has been removed. """

    def delete(self):
        # remove the topmost value from heap
        deleted = self.storage.pop(0)

        for i in range(0, len(self.storage)):
            self._bubble_up(i)

        return deleted

    """ get_max returns the maximum value in the heap in constant time."""

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        print("Size: ", len(self.storage))
        return len(self.storage)

    """ _bubble_up moves the element at the specified index "up" the heap by swapping it with its parent if the parent's value is less than the value at the specified index (if parent < child, swap )."""

    def _bubble_up(self, index):
        while index > 0:
            # identify parent
            parent = (index - 1) // 2

            # compare: if child is greater than parent
            if self.storage[index] > self.storage[parent]:
                # swap
                # indicating that this a max heap
                # since we want the higher value on top
                self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]

                # now update the index (change node so while loop can keep going)
                index = parent

            else:
                break

    def _sift_down(self, index):
        pass
