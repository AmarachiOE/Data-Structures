Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?
O(1) - constant time

2. What is the runtime complexity of `dequeue`?
O(1) - constant time

3. What is the runtime complexity of `len`?
O(1) - constant time

## Binary Search Tree

1. What is the runtime complexity of `insert`? 
O(log n) - logarithmic time

2. What is the runtime complexity of `contains`?
O(log n) - logarithmic time

3. What is the runtime complexity of `get_max`? 
O(log n) - logarithmic time

## Heap

1. What is the runtime complexity of `_bubble_up`?
O(n) - linear time

2. What is the runtime complexity of `_sift_down`?
O(n) - linear time

3. What is the runtime complexity of `insert`?
O(n) - linear time

4. What is the runtime complexity of `delete`?
O(n^2) - quadratic time, contains recursion nested inside for loop

5. What is the runtime complexity of `get_max`?
O(1) - constant time

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?
O(1) - constant time

2. What is the runtime complexity of `ListNode.insert_before`?
O(1) - constant time

3. What is the runtime complexity of `ListNode.delete`?
O(1) - constant time

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
O(1) - constant time

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
O(1) - constant time

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
O(1) - constant time

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
O(1) - constant time

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
O(1) - constant time

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
O(1) - constant time

10. What is the runtime complexity of `DoublyLinkedList.delete`?
O(1) - constant time

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?
    worst case for `Array.splice()` is O(n). So the Linked List's `.delete()` method performs better.