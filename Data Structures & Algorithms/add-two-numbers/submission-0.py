# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d1, d2 = deque(), deque()

        # initial pass, add values to deques
        while l1 or l2:
            if l1:
                d1.append(l1.val)
                l1 = l1.next
            if l2:
                d2.append(l2.val)
                l2 = l2.next
        
        # leftmost value of the deque is the first node
        carryover = 0
        head = curr = ListNode(carryover)
        i = 0
        while d1 or d2:
            # initialize the variables
            val1 = val2 = 0

            print(i, "d1 pre:", d1)
            print(i, "d2 pre:", d2)

            # pop values from deque if exist
            if d1: val1 = d1.popleft()
            if d2: val2 = d2.popleft()

            print(i, "val1:", val1)
            print(i, "val2:", val2)

            print(i, "d1 post:", d1)
            print(i, "d2 post:", d2)

            # calculate the total and carryover if exists
            total = val1 + val2 + carryover

            if total >= 10: 
                carryover = 1 
            else: 
                carryover = 0

            total = total % 10

            # update the value of the current node
            curr.val = total

            # add a new node and iterate if values still exist
            if d1 or d2 or carryover == 1: 
                curr.next = ListNode(carryover)
                curr = curr.next
            i += 1
            print()
            
        return head