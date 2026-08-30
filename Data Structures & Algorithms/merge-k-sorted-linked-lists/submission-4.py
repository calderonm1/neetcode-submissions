# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                
                mergedLists.append(self.mergeLists(l1, l2))

            lists = mergedLists

        return lists[0]

    def mergeLists(self, l1, l2):
        dummy = head = ListNode()
        while l1 is not None or l2 is not None:
            minVal = 0
            if l1 is not None and l2 is not None:
                if l1.val < l2.val:
                    minVal = l1.val
                    l1 = l1.next
                else:
                    minVal = l2.val
                    l2 = l2.next
            elif l1 is not None:
                minVal = l1.val
                l1 = l1.next
            else:
                minVal = l2.val
                l2 = l2.next

            head.next = ListNode(minVal)
            head = head.next

        return dummy.next