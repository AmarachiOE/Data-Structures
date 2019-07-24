class BinarySearchTree:  # think BinarySearchTreeNode
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value == self.value or self.value is None:
            self.value = value

        elif value < self.value:
            # create new node # BinarySearchTreeNode(value)
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:  # recursion
                self.left.insert(value)

        else:  # value > self.value:
            # create new node # BinarySearchTreeNode(value)
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:  # recursion
                self.right.insert(value)

    def contains(self, target):
        if self.value is None or self.value == target:
            return True  # return self.value

        elif target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)  # recursion

        else:
            # if target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)  # recursion

    def get_max(self):

        if self.value is None:
            return 0

        else:
            root_max = self.value

            if self.right is None:
                rbranch_max = 0
            else:
                rresult = self.right.get_max()
                rbranch_max = rresult

            if self.left is None:
                lbranch_max = 0
            else:
                lresult = self.left.get_max()
                lbranch_max = lresult

        return max([root_max, rbranch_max, lbranch_max])

    def for_each(self, cb):
        if self.value:  # if exists or != None
            cb(self.value)

            if self.left:
                self.left.for_each(cb)

            if self.right:
                self.right.for_each(cb)
