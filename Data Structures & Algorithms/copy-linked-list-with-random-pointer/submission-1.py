"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        originalToCopy = {}
        current = head

        while current:
            copy = Node(current.val)
            originalToCopy[current] = copy
            current = current.next

        dummy_head_copy = originalToCopy.get(head)

        while head:
            if head.random: originalToCopy[head].random = originalToCopy[head.random]
            if head.next: originalToCopy[head].next = originalToCopy[head.next]
            head = head.next

        return dummy_head_copy
            
        