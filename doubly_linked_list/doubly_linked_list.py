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
        self.next = ListNode(value, self, current_next)  # wrapping
        if current_next:  # if current item already has next item
            # inserting this next value before (prev) the new items "current_next"
            current_next.prev = self.next

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

        if self.head == None:  # our LL is empty
            self.head = new_node
            self.tail = new_node

        else:  # LL is not empty
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
            new_node.prev = self.tail
            self.tail.next = new_node
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
        self.add_to_head(node.value)
        self.delete(node)  # delete original reference to node

    def move_to_end(self, node):
        self.add_to_tail(node.value)
        self.delete(node)

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
        # check if head is None before all
        if self.head == None:
            return None

        max = self.head.value
        current = self.head

        while current:
            if current.value > max:
                max = current.value
            current = current.next

        print("Max value: ", max)
        return max
