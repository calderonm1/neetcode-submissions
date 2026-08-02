# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head2 = None
        prev = None
        
        while head:
            head2 = ListNode(head.val)
            head2.next = prev
            prev = head2
            head = head.next

        return head2
